import aiohttp
from lxml import etree
import asyncio
import aiomysql
from asyncio import Queue

start_url = "https://www.smzdm.com/fenlei/zhinengshouji/"
queue = Queue()
seen_urls = set()
stop = False


async def fetch(url, session):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    try:
        async with session.get(url, headers=headers) as resp:
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)

async def extract_url(text):
    html = etree.HTML(text)
    urls = html.xpath("//ul/li//h5/a/@href")
    for url in urls:
        if url not in seen_urls:
            seen_urls.add(url)
            await queue.put(url)
    return urls

async def init_urls():
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        await extract_url(html)

async def save_to_mysql(pool, title):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            sql = "insert into asyncio (title) values ({!r})".format(title)
            print(sql)
            await cur.execute(sql)

async def consumer(pool):
    while not stop:
        url = await queue.get()
        async with aiohttp.ClientSession() as session:
            text = await fetch(url, session)
            html = etree.HTML(text)
            title = html.xpath("//h1[@class='title J_title']/text()")[0]
            if title:
                asyncio.ensure_future(save_to_mysql(pool, title.strip())) # 理解为协程池

async def main(loop):
    pool = await aiomysql.create_pool(
        host='47.96.156.199', port=3306, user='root', password='Qazwsx@123', db='test', loop=loop, charset='utf8',
        autocommit=True,
    )
    asyncio.ensure_future(init_urls())
    asyncio.ensure_future(consumer(pool))

    # 不能async with .. as session: 下边两个ensure, 因为会退出上下文，导致session 关闭，而池中还在使用


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()

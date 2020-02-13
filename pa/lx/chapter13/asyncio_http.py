

# asyncio 没有提供http协议的接口，可以使用aiohttp
import socket
from urllib.parse import urlparse
import asyncio


async def get_html(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf-8")
        all_lines.append(data)

    html_data = ''.join(all_lines)
    return html_data

async def main():
    # 完成一个task，获取一个task的结果，需要如下写
    tasks = []
    for _ in range(20):
        url = "http://www.baidu.com"
        tasks.append(asyncio.ensure_future(get_html(url)))
    for task in asyncio.as_completed(tasks):
        result = await task # task是一个协程，所以要用await
        print(result)


if __name__ == '__main__':
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = []
    # for i in range (20):
    #     tasks.append(get_html("http://www.baidu.com"))
    # loop.run_until_complete(asyncio.wait(tasks))

    # -----------------------------------------
    # 为了得到结果，需要从future对象中获取
    # for i in range(20):
    #     tasks.append(asyncio.ensure_future(get_html("http://www.baidu.com")))
    # loop.run_until_complete(asyncio.wait(tasks)) # 可以保持不变，wait可以接收task, future对象
    #
    # for task in tasks:
    #     print(task.result())
    # print(time.time() - start)

    # -----------------------------------------
    # 完成一个task从一个task中获取结果
    loop.run_until_complete(main())
    print(time.time() - start)

# python 原生协程
# async不能出现yield, yield from
# 协程我们使用async来实现

# await 后面跟awaitable的对象
# 只要实现 def __await__(self): 方法
# 可以将 await 理解为yield from


from collections import Awaitable
import types

@types.coroutine
def downloader1(url):
    yield "zzlion"

async def downloader(url):
    return "zzlion"

async def download_url(url):
    # html = await downloader(url)
    html = await downloader(url)
    return html

if __name__ == '__main__':
    coro = download_url("http://www.baidu.com")
    # next(coro) # async语法中不能使用next
    coro.send(None)
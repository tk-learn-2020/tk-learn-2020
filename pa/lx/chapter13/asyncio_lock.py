
import asyncio

# total = 0
#
# async def add():
#     global total
#     for i in range(10000):
#         total += 1
#
# async def desc():
#     global total
#     for i in range(10000):
#         total -= 1
#
# if __name__ == '__main__':
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

# -----------------------------------------
import aiohttp
from asyncio import Lock, Queue

queue = Queue()
await queue.put(1)

# 在不考虑 限流的情况下可以如下使用
queue = []

cache = {}
lock = Lock()

async def get_stuff(url):
    await lock.acquire()
    if url in cache:
        return cache[url]
    stuff = await aiohttp.request("get", url)
    cache[url] = stuff
    lock.release()

    # 使用上下文
    # async with lock: 这种用法是由于实现了 __aenter__, __aexit__, __await__方法
    # with await lock: 这种用法是由于实现了 __enter___, __exit__ 方法

    # __await__ 方法最终会调用 acquire方法，其中的 _lock通过属性实现，因为协程是单线程， 多线程的锁才用到了系统底层的锁

    return stuff

async def parse_stuff():
    stuff = await get_stuff("")
    # do something

async def use_stuff():
    stuff = await get_stuff("")
    # do something

# 这种场景中 parse_stuff与use_stuff可能会请求到相同的url，所以需要同步机制

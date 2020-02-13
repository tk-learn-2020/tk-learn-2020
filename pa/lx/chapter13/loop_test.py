# 事件循环 + 回调（驱动生成器）+epoll（IO多路复用）

import asyncio
import time
from functools import partial

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    # 不能使用阻塞的 time.sleep()
    # await time.sleep(2)
    # time.sleep(2), 使用这个在多次执行的任务中，每个任务sleep2s
    print("end get url")
    return "zzlion"

def callback(url, future):
    print(url)
    print("send email to zzlion")

if __name__ == '__main__':
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("http://www.baidu.com")) # 可以理解为多线程的join, 把asyncio理解为协程池
    # print(time.time() - start_time)

    # -----------------------------------------
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.baidu.com") for i in range(100)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.time() - start_time)
    # # asyncio.wait是一个协程, 对应于线程池的wait, 里边有参数return_when

    # -----------------------------------------
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.baidu.com") for i in range(100)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    # gather 与 wait 的区别
    # gather 更加 high-level, 更加灵活，可以优先使用
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # group1_tasks = [get_html("http://www.baidu.com") for i in range(2)]
    # group2_tasks = [get_html("http://www.baidu.com") for i in range(3)]
    # loop.run_until_complete(asyncio.gather(*group1_tasks, *group2_tasks))
    # 或者
    group1_tasks = [get_html("http://www.baidu.com") for i in range(2)]
    group2_tasks = [get_html("http://www.baidu.com") for i in range(3)]
    group1_tasks = asyncio.gather(*group1_tasks)
    group2_tasks = asyncio.gather(*group2_tasks)
    group1_tasks.cancel()
    loop.run_until_complete(asyncio.gather(group1_tasks, group2_tasks))
    print(time.time() - start_time)

    # -----------------------------------------
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())
    # print(time.time() - start_time)

    # -----------------------------------------
    # # task是future的子类，future的功能，task都有
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(get_html("http://www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())
    # print(time.time() - start_time)

    # -----------------------------------------
    # 添加回调函数, 在return之前调用callback函数, 与课程不一致
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(get_html("http://www.baidu.com"))
    # task.add_done_callback(partial(callback, "http://www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())
    # print(time.time() - start_time)

    # # learn:partial函数的作用
    # """
    # 一般函数在执行时，需要带上必要的参数调用，但有时参数可以在函数被调用之前提前获知，此时，一个函数有一个或多个参数预先就可以用上，以便函数能用更少的参数进行调用
    # """
    # def add(a, b):
    #     print(a)
    #     print(b)
    #     return a + b
    # fun1 = partial(add, 2)
    # fun1(3)





import asyncio

def fun(sleep_times):
    print("seleep {} success".format(sleep_times))

def stop_loop(loop):
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # -----------------------------------------
    # loop.call_soon(fun, 2)
    # loop.call_soon(stop_loop, loop)
    # loop.run_forever() # 因为不是一个协程，所以用这种方式启动

    # -----------------------------------------
    # # 在一定延时后运行, call_soon比call_later先运行, call_later内部调用的call_at
    # loop.call_later(1, fun, 1)
    # loop.call_later(3, fun, 3)
    # loop.call_later(2, fun, 2)
    # # loop.call_soon(stop_loop, loop)
    # loop.call_soon(fun, 4)
    # loop.run_forever() # 因为不是一个协程，所以用这种方式启动

    # -----------------------------------------
    # # 在一定延时后运行, call_soon比call_later先运行, call_later内部调用的call_at
    def fun(loop):
        print("seleep {} success".format(loop.time()))

    def stop_loop(loop):
        loop.stop()

    now = loop.time()
    loop.call_at(now + 1, fun, loop)
    loop.call_at(now + 3, fun, loop)
    loop.call_at(now + 2, fun, loop)
    # loop.call_soon(stop_loop, loop)
    loop.call_soon(fun, loop)
    loop.run_forever() # 因为不是一个协程，所以用这种方式启动

    # -----------------------------------------
    # loop.call_soon_threadsafe 在多线程中使用

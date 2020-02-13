import asyncio

# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# 1. loop 会被放到future当中(asyncio 设计模式：将loop放到future中，将future放到loop中，形成环状)
# 2. 取消future(task)

import asyncio
import time

async def get_html(sleep_tiems):
    print("waiting")
    await asyncio.sleep(sleep_tiems)
    print("done after {}s".format(sleep_tiems))

if __name__ == '__main__':
    task1 = get_html(1)
    print(task1)
    task2 = get_html(2)
    task3 = get_html(3)

    tasks = [task1, task2, task3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print(task)
            print("task cancel")
            print(task.cancel())
        loop.stop()
        loop.run_forever() # caution: 取消任务这步很重要
    finally:
        loop.close()

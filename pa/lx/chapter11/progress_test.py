# 多进程编程
# 计算密集型使用多进程， io密集型使用多线程

def fib(num):
    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time

# with ThreadPoolExecutor(3) as executor:
with ProcessPoolExecutor(6) as executor:
    all_tasks = [executor.submit(fib, num) for num in range(24, 40)]
    start = time.time()
    for future in as_completed(all_tasks):
        data = future.result()
        print("exe result: {}".format(data))
    print("last time is :{}".format(time.time() - start))

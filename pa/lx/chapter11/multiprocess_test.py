# import os
# import time
# # fork 只能用于unix
# # 子进程会运行fork之后的代码
# print("zzlion")
# pid = os.fork()
# # print("zzlion")
# if pid == 0:
#     print("子进程：{}，父进程：{}".format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程：{}".format(os.getpid()))
## 教程中没有time.sleep子进程就不会退出，实际测试不符
# time.sleep(2)

# -----------------------------------------
# 多进程更推荐concurrent.futures.ProcessPoolExecutor
# multiprocessing更加底层

import time
import multiprocessing

def get_html(n):
    print("sub progress start")
    time.sleep(n)
    return n

# def main():
#     progress = multiprocessing.Process(target=get_html, args=(3,))
#     print(progress.pid) # 开始之前是None
#     progress.start()
#     print(progress.pid) # 开始之后有正常id
#     progress.join()
#     print("main progress end")

# -----------------------------------------
# 使用进程池
# pool = multiprocessing.Pool(multiprocessing.cpu_count())
# result = pool.apply_async(get_html, args=(3,))  # 返回类似Future的对象
# # caution: 一定要关闭pool，否则可能报Pool is still running的错误
# pool.close()
# # 等待所有任务完成
# pool.join()
# print(result.get())

# -----------------------------------------
# imap,对应于executor.map方法
pool = multiprocessing.Pool(multiprocessing.cpu_count())
# for result in pool.imap(get_html, [1, 3, 2]):
#     # 打印顺序与列表顺序一致
#     print("{} sleep success".format(result))

# imap_unordered
for result in pool.imap_unordered(get_html, [1, 3, 2]):
    # 打印顺序不确定
    print("{} sleep success".format(result))



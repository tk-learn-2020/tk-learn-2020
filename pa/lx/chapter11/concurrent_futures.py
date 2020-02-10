# 功能简单，但是理念值得学习

# -----------------------------------------
# 为什么要使用线程池？
# 1.主线程可以获取任意一个线程的状态或某一个任务的状态，以及返回值
# 2.当一个线程完成的时候，主线程可以立即知道
# 3. futures可以让多线程与多进程接口一致

# 如果获取执行成功的task
# as_completed
# executor.map()

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
import time

def get_html(times, value=0):
    time.sleep(times)
    print("get page {} success.".format(times))
    # print(value)
    return times


executor = ThreadPoolExecutor(max_workers=2)

# -----------------------------------------
# # 通过submit函数提交执行的函数到线程池中
# # submit 非阻塞，立即返回
# # caution：这里传递参数不用元组，即不加逗号
# task1 = executor.submit(get_html, 3, 3) # task1 Future类对象
# task2 = executor.submit(get_html, 2, 2)
#
# # # done 方法判定函数是否执行完
# # print(task1.done())
# # # 只有在任务没有开始的情况下可以取消，e.g. max_workers改为1的时候
# # print(task2.cancel())
# # time.sleep(3)
# # print(task1.done())
# #
# # #result获取task执行结果
# # print(task1.result())

# -----------------------------------------
# 获取已经成功的task的返回
# # 遍历as_completed的时候会阻塞，all_tasks里边全部完成以后才会结束as_completed
# urls = [1, 2, 3, 4]
# all_tasks = [executor.submit(get_html, i) for i in urls]
# for future in as_completed(all_tasks):
#     ret = future.result()
#     print(ret)

# -----------------------------------------
# # 通过executor获取已经成功的task
# urls = [2, 1, 3, 4]
# # 此处的map与python的map类似
# for ret in executor.map(get_html, urls):
#     # caution: 执行print的循序与 urls的顺序一致，但是任务根据实际情况执行
#     print("ret:{}".format(ret))

# -----------------------------------------
# urls = [2, 1, 3, 4]
# all_tasks = [executor.submit(get_html, i) for i in urls]
# # wait让主线程阻塞，可以等待一个或多个task, 默认所有完成以后
# wait(all_tasks, return_when=FIRST_COMPLETED)
# print("main") # 在第一个task执行完以后就会执行到这里

# -----------------------------------------
task = executor.submit(get_html, 3)
# task未来对象，task的返回容器, 线程池，进程池，协程使用相同的设计理念
# 分析submit方法的源码，1)学习用上下文管理器，管理线程锁 2)返回Future对象 3)学习Future对象的方法
# 1)
# lock = Threading.Lock()
# with lock:
#   ...

# 2)
"""
数据流:
_WorkItem包含了Future对象，fun及其参数，对象w放入线程共享的queue
submit方法中调用的_adjust_thread_count方法 控制启动线程，线程启动_worker方法
_worker方法通过死循环从队列中获取对象w, 执行对象w的run方法，
w的run方法, run方法执行fun，并将fun的结果设置到f对象
"""
# 3)
# 回顾condition的内容, RLock(reentrant lock) 可重进入锁
# 重点：result, set_result方法
# result阻塞方法，有timeout参数
# set_result中的waiter涉及之前用到的wait, e.g. _FirstCompletedWaiter(其中涉及到了threading.event, 也是一把锁)
# 查看event的源码并了解



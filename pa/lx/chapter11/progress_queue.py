from multiprocessing import Process, Queue, Pool, Manager, Pipe
# from queue import Queue # 程序不会停止了？
import time

def producer(queue, a):
    a += 100
    queue.put("a")
    time.sleep(2)

def consumer(queue, a):
    time.sleep(2)
    data = queue.get()
    print(data)
    print(a)

# queue = Queue()
# a = 1
# my_producer = Process(target=producer, args=(queue, a))
# my_consumer = Process(target=consumer, args=(queue, a))
# my_producer.start()
# my_consumer.start()
# my_producer.join()
# my_consumer.join()

# -----------------------------------------
# 共享全局变量无法在多进程中使用，适用于多线程

# -----------------------------------------
# multiprocess.Queue不能用于pool进程池, 只能使用manager中的Queue
# queue = Queue(10)
# queue = Manager().Queue(10)
# pool = Pool(2)
# a = 1
# pool.apply_async(producer, args=(queue, a))
# pool.apply_async(consumer, args=(queue, a))
# pool.close()
# pool.join()

# -----------------------------------------
# Pipe简化版的Queue, 实现进程间通信
# Pipe只适用于两个进程间通讯
# Pipe 性能比 Queue高
# def producer(pipe):
#     pipe.send("a")
#     time.sleep(2)
#
# def consumer(pipe):
#     time.sleep(2)
#     data = pipe.recv()
#     print(data)
#
# receive_pipe, send_pipe = Pipe()
# my_producer = Process(target=producer, args=(send_pipe,))
# my_consumer = Process(target=consumer, args=(receive_pipe,))
# my_producer.start()
# my_consumer.start()
# my_producer.join()
# my_consumer.join()

# -----------------------------------------
# 进程间操作相同内存上的数据
# 使用共享内存数据要注意同步问题
def add_data(p_dict, key, value):
    p_dict[key] = value

process_dict = Manager().dict()
first_progress = Process(target=add_data, args=(process_dict, 'name', 'lixiong'))
second_progress = Process(target=add_data, args=(process_dict, 'age', 17))
first_progress.start()
second_progress.start()
first_progress.join()
second_progress.join()
print(process_dict)

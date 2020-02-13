import itertools

my_list = [1, 2, 3]
my_dict = {"name": "zzlion", "age": 17}

# for value in itertools.chain(my_list, my_dict, range(5, 8)):
#     print(value)

def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable

# for value in my_chain(my_list, my_dict, range(5, 8)):
#     print(value)


def gen1(gen):
    yield from gen

def main():
    a = (for i in range(10))
    gen = gen1(a)
    next(gen)

# 概念： main 调用方，gen1委托生成器，gen子生成器
# yield from  在调用方与子生成器之间建立双向通道

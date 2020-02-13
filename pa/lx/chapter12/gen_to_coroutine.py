# 生成器可以暂停

import inspect

def fun():
    value = yield 1
    yield 2
    return "zzlion"

if __name__ == '__main__':
    gen = fun()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except Exception as e:
        pass
    print(inspect.getgeneratorstate(gen))



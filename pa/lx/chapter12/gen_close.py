
def gen_func():
    try:
        html = yield "http://www.baidu.com"
        print(html)
    # except GeneratorExit as e:
    except BaseException as e:
        # raise StopIteration
        pass
    yield 2
    yield 3
    return "zzion"

if __name__ == '__main__':
    gen = gen_func()
    # -----------------------------------------
    # ret = gen.send(None)
    # print(ret)
    # ret = gen.send('hello world')
    # print(ret)

    # -----------------------------------------
    print(next(gen))
    gen.close()
    print(next(gen)) # StopIteration

    # 如果在yied 处捕捉了 GeneratorExit 异常，则会在gen.close处报异常, 因为后续任然有yield语句，否则则会报StopIteration
    #Traceback (most recent call last):
    #   File "/home/zzlion/projects/tk-learn-2020/pa/lx/chapter12/gen_close.py", line 22, in <module>
    #     gen.close()
    # RuntimeError: generator ignored GeneratorExit

    # GeneratorExit 继承自BaseException; Exception 继承自Exception

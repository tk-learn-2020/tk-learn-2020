
def func():
    try:
        yield "http://www.baidu.com"
    except Exception as e:
        print(e)
    yield 2
    yield 3
    return "zzlion"

if __name__ == '__main__':
    gen = func()
    print(next(gen))
    gen.throw(Exception, "yield error")
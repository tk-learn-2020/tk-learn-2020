'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-05
@Desc   :  单例模式装饰器
'''



def single_decorator(cls):
    _instance = None

    def inner(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = cls(*args, **kwargs)
        return _instance
    return inner

@single_decorator
class Singleton(object):
    pass

# 示例：
a = Singleton()
b = Singleton()

print(a)
print(b)
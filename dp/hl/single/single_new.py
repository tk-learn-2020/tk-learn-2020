'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-05
@Desc   :   单例模式

'''

"""通过__new__实现单例"""


class Single(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Single()
obj2 = Single()
print(obj1)
print(obj2)
# 类也是对象，type创建类的类

def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# -----------------------------------------
# type 动态创建类
class BaseClass:
    def answer(self):
        return "i am baseclass"

def say(self):
    return "fine"

User = type("User", (BaseClass,), {"name": "user", "say": say})

# -----------------------------------------
# 什么是元类，元类就是创建类的类，type是一个元类，

# python 中类的实例化过程, 首先会查找metaclass,通过metaclass创建User类, 找不到了则去基类查找
# type去创建类对象

class MetaClass(type):
    # 这个就是元类, 元类控制实例化的过程
    def __new__(cls, *args, **kwargs):
        # caution: 这里要把 实例的实例化参数传进来
        return super().__new__(cls, *args, **kwargs)

class Person(metaclass=MetaClass):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"

# -----------------------------------------
from  collections.abc import *
# 里边有很多metaclass

if __name__ == '__main__':
    # -----------------------------------------
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    # -----------------------------------------
    # my_obj = User()
    # print(my_obj)
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer())

    # -----------------------------------------
    persion = Person("zzlion")
    print(persion)



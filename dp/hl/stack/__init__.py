'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-11
@Desc   :  代理模式

'''


"""把一个对象的操作代理到另一个对象"""

from collections import deque
class TestStack:
    def __init__(self):
        self._stack = MyTest()

    def add(self, value):
        return self._stack.add(value)

    def append(self, value):
        return self._stack.append(value)

    def delete(self, value):
        return self._stack.delete(value)


class MyTest:
    def append(self, *args, **kwargs):
        print("append")

    def add(self, *args, **kwargs):
        print("add")

    def delete(self, *args, **kwargs):
        print("delete")
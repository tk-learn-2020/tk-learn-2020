'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-13
@Desc   :   共享模式

'''


class Borg:
    __shared_state = {}

    state = None

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':

    # 两个实例对象是共享的
    test1 = Borg()
    test2 = Borg()

    test1.state = 'test1'
    test2.state = 'test2'    # test2重新赋值后，test1也变了

    print('test1:', test1)
    print('test2:', test2)

    test2.state = 'test22'

    print('test1:', test1)
    print('test2:', test2)

    print('id of test1:', id(test1))
    print('id of test2:', id(test2))

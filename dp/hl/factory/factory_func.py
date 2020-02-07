'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-06
@Desc   :   工厂方法

'''


"""
是对简单工厂模式的改进，将工厂分成多个具体的工厂，
这样每个子工厂只需要继承父工厂即可，不需要改动父工厂

"""


class BW:
    def __init__(self):
        pass


class BJXD:
    def __init__(self):
        pass


class BC:
    def __init__(self):
        pass


class CarFactory:
    """父类工厂"""
    def product_car(self):
        print("this is parent factory")


class BWFactory(CarFactory):
    """宝马工厂"""
    def product_car(self):
        print("this is BW factory")
        return BW()


class BCFactory(CarFactory):
    """奔驰工厂"""
    def product_car(self):
        print("this is BC factory")
        return BC()


class BJXDFactory(CarFactory):
    """北京现代工厂"""
    def product_car(self):
        print("this is BJXD factory")
        return BJXD()


bw = BWFactory().product_car()
print(bw)
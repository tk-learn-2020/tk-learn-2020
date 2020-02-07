'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-06
@Desc   :   抽象工厂模式

'''


"""抽象工厂中的一个工厂对象可以负责多个不同产品对象的创建"""


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

    # 小轿车
    def product_car(self):
        print("this is parent car factory")
    #suv
    def product_suv_car(self):
        print("this is parent suv factory")



class BWFactory(CarFactory):
    """宝马工厂"""
    def product_car(self):
        print("this is BW car factory")
        return BW()

    def product_suv_car(self):
        print("this is BW suv factory")


class BCFactory(CarFactory):
    """奔驰工厂"""
    def product_car(self):
        print("this is BC car factory")
        return BC()

    def product_suv_car(self):
        print("this is BC suv factory")


class BJXDFactory(CarFactory):
    """北京现代工厂"""
    def product_car(self):
        print("this is BJXD car factory")
        return BJXD()

    def product_suv_car(self):
        print("this is BJXD suv factory")
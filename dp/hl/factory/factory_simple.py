'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-06
@Desc   :   简单工厂模式

'''

"""
简单工厂模式适用于需创建的对象较少
缺点：如果要新增需要改动工厂类，比如加一个性别:未知 的类
"""

class Male:
    def __init__(self,name):
        self.name = name or None
        self.gender = "男"
        print("my name is {}，i am {}".format(self.name,self.gender))


class Female:
    def __init__(self,name):
        self.name = name
        self.gender = "女"
        print("my name is {}，i am {}".format(self.name, self.gender))



class SimpleFactory:
    def gen_person(self, name, gender):
        if gender == '男':
            return Male(name=name)
        if gender == '女':
            return Female(name=name)



# 这样就不用了各自去实例化了，走工厂即可
if __name__ == '__main__':
    factory = SimpleFactory()
    person = factory.gen_person("张三","男")
    person2 = factory.gen_person("菜花","女")
    print(person)
    print(person2)


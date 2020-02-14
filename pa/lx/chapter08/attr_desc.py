import numbers

class IntField:
    """ 实现任意一个下列方法都是属性描述符 """
    # 实现了 __get__ 与 __set__ 为数据描述符

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataStrField:
    # 只实现了__get__为非数据描述符

    def __get__(self, instance, owner):
        return "non data"

class User:
    age = IntField()
    school = 'jingsheng'
    nondata = NonDataStrField()

if __name__ == '__main__':
    user = User()
    user.age = 19
    # -----------------------------------------
    # 数据描述符会进入类的__dict__当中, 不会进入实例的__dict__
    print(User.__dict__)
    print(user.__dict__)

    # -----------------------------------------
    # 数据描述符的查找最高，然后查找实例的属性，最后是类的
    # 非数据描述符
    user.__dict__['age'] = 20
    print(user.age)
    print(user.nondata)
    user.__dict__['nondata'] = "fine"
    print(user.nondata)

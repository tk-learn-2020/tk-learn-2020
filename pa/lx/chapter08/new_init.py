# new 控制对象生成过程，在对象生成之前
# init 是完善对象
# new没有return 的话不会调用init方法
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    def __init__(self, name):
        print("in init")
        self.name = name

if __name__ == '__main__':
    user = User("zzlion")

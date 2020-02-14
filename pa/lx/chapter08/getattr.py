# __getattr__, __getattribute__
# __getattr__ 在查找不到属性时调用
# __getattribute__是所有属性从这里查找

class Persion:

    def __init__(self, name, bitthday, info:dict=None):
        self.name = name
        self.birthday = bitthday
        self.info = info

    def __getattr__(self, item):
        return  self.info.get(item)

    def __getattribute__(self, item):
        return "zzlion"

if __name__ == '__main__':
    persion = Persion('zzlion', 18, {'school': 'jingsheng'})
    print(persion.name)
    print(persion.school)



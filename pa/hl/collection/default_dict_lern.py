'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-07
@Desc   :

'''


from collections import defaultdict

test_dict = {}
lista = ['test','ceshi','test','ceshi','test']

for test in lista:
    # 这里不用去判断是不是已经存在key
    test_dict.setdefault(test,0)
    test_dict[test] += 1

print(test_dict)



# defaultdict
default_dict = defaultdict(int)  # 当不存在key的时候使用指定的对象,int默认是0
for test in lista:
    default_dict[test] += 1

print(default_dict)


# dict嵌套dict
def gen_default_dict():
    return {'name':'','age':''}

default_dict = defaultdict(gen_default_dict)
print(default_dict["name"])
print(default_dict["test"])





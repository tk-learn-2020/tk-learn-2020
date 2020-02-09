'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-07
@Desc   :

'''

from collections import namedtuple

# 相当于类的实例化，创建了一个Student类，一般用于数据库
Student = namedtuple("Student",['name','age','cla'])

user = Student("hallen",18,3)

print(user)
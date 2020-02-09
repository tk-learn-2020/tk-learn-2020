'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-07
@Desc   :

'''


fp = open("test.txt",'r',encoding='utf-8')
fp.seek(0,2)
end = fp.tell()
print(end)
temp = end-2
fp.seek(temp,0)
text = fp.read()
print(text)

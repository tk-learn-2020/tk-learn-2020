'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-11
@Desc   :

'''


from multiprocessing import Process
AGE = 1
def hello():
    print("hello")
def hallen(names):
    global AGE
    AGE += 1
    names.append('hallen')
    print('=====子进程=====')
    print('AGE：%d，id：%s' % (AGE,id(AGE)))
    print('names:%s' %names)
    print(id(hello))
    print('=====子进程=====')

if __name__ == '__main__':
    names = ['hailong']
    p = Process(target=hallen,args=(names,))
    p.start()
    p.join()

    print('=====父进程=====')
    print('AGE：%d，id：%s' % (AGE, id(AGE)))
    print('names:%s' % names)
    print(id(hello))
    print('=====父进程=====')
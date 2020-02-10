'''
@Author  : hallen
@Contact :  hallen200806@163.com
@Time   :   2020-02-10
@Desc   :

'''


"""
用户都订阅了一位新闻发布者，当新闻发布者发布了一个新的新闻后，
他就会通知它的所有订阅者，就像是手机上一些应用的通知栏通知

缺点：关联性强
"""


class NewsPublisher:
    """新闻发布者"""
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self,subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update(self.__latestNews)

    def addNews(self,news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News:'+self.__latestNews


class ConcreteSubscriber1:           #ConcreteObserver
    def __init__(self,publisher):
        self.publisher=publisher
        self.publisher.attach(self)

    def update(self,news):
        print(type(self).__name__,news)

class ConcreteSubscriber2:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self,news):
        print(type(self).__name__, news)

news_publisher = NewsPublisher()

#创建观察者对象
for Subscribers in [ConcreteSubscriber1,ConcreteSubscriber2]:
    Subscribers(news_publisher)

news_publisher.addNews('hello subscibers')
news_publisher.notifySubscribers()
news_publisher.detach()
news_publisher.addNews('hi subscibers')
news_publisher.notifySubscribers()
news_publisher.detach()
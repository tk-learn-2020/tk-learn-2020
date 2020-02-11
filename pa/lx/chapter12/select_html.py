# 并发高，连接活跃度不高，epoll比select好
# 并发不高，连接活跃，select 比epoll好
import socket
from urllib.parse import urlparse
# import select # 一般不直接使用select, selectors包装之后更容易使用，同时内部对使用poll还是epoll根据系统平台自适应
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:

    def get_html(self, url):
        self.request_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == '':
            self.path = '/'

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False) # 设置非阻塞以后需要捕捉异常
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册
        # 参数: fileobj, events, data
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # 只要socket状态是可读，就会一直回调这个函数
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)

            data = self.data.decode("utf-8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

            urls.remove(self.request_url)
            if not urls:
                global stop
                stop = True

def loop():
    # 事件循环，不停的请求socket的状态，并调用对应的回调函数
    # 1.select模块本身不支持register功能
    # 2.socket状态变化以后的回调由程序员完成，即本函数的作用
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调 + 事件循环 + select +(poll/epoll)

if __name__ == '__main__':
    fetcher = Fetcher()
    for url in urls:
        fetcher.get_html(url)
        loop()

import socket
from urllib.parse import urlparse

def get_html(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False) # 设置非阻塞以后需要捕捉异常
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    # client.connect背后还会继续连接
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""

    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == '__main__':
    get_html("http://www.baidu.com")
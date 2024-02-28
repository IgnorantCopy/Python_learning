import urllib.request

import gevent
from gevent import monkey

monkey.patch_all()


def download(url):
    response = urllib.request.urlopen(url)
    text = response.read()
    print("Downloading {} data in {}".format(len(text), url))


if __name__ == '__main__':
    urls = ["https://www.163.com", "https://www.baidu.com", "https://www.qq.com"]
    gevent1 = gevent.spawn(download, urls[0])
    gevent2 = gevent.spawn(download, urls[1])
    gevent3 = gevent.spawn(download, urls[2])

    gevent.joinall([gevent1, gevent2, gevent3])

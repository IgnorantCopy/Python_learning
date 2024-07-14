"""
Created by Ignorant on 2024/7/12
Description: URL管理器
"""


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_url(self, url):
        if url is None or len(url) == 0 or url in self.old_urls or url in self.new_urls:
            return
        self.new_urls.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    def get_url(self):
        if self.has_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        return None

    def has_url(self):
        return len(self.new_urls) > 0


if __name__ == '__main__':
    url_manager = UrlManager()
    url_manager.add_urls(['http://www.baidu.com', 'http://www.sina.com.cn', 'http://www.sohu.com'])
    while url_manager.has_url():
        print(url_manager.get_url())

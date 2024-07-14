"""
Created by Ignorant on 2024/7/12
Description: 使用BeautifulSoup解析网页
"""
from bs4 import BeautifulSoup as bs

with open("test.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

# 根据网页字符串创建 BeautifulSoup 对象
soup = bs(html_doc,  # 网页字符串
          "html.parser",  # HTML 解析器
          from_encoding="utf-8")  # 网页编码
'''
搜索节点：
soup.find_all(name, attrs, string): 返回所有符合条件的节点
soup.find(name, attrs, recursive, text, **kwargs): 返回第一个符合条件的节点
'''
div_node = soup.find("div", id="content")
print(div_node)
print('-' * 50)
links = div_node.find_all("a")
image = div_node.find("img")
'''
节点信息：
    node.name: 标签名称
    node[attr]: 属性值
    node.get_text(): 节点内所有文本内容
'''
for link in links:
    print(link.name, link['href'], link.get_text())
print('-' * 50)
print(image['src'])

"""
Created by Ignorant on 2024/7/12
Description: Requests module
"""
import requests

'''
requests.get/post(url, params=None, data=None, headers=None, verify=True, cookies=None, timeout=None, allow_redirects=True)
    url: 请求的url地址
    params: 请求的参数
    data: 请求的数据
    headers: 请求的头部信息
    verify: 是否验证 HTTPS 证书
    cookies: 请求的 cookie 信息
    timeout: 请求的超时时间(单位: 秒)
    allow_redirects: 是否允许重定向
'''
request = requests.get('https://www.baidu.com')
'''
request.status_code: 获取响应状态码
request.encoding: 获取响应的编码方式(requests 会根据 Header 推测编码，推测不到会设置为 ISO-8859-1，导致中文乱码)
request.text: 获取响应的网页内容
request.headers: 获取响应的头部信息
request.url: 获取请求的 url 地址
request.content: 获取响应的二进制内容(可以用于下载图片)
request.cookies: 获取响应的 cookie 信息
'''
print(request.status_code)
print(request.encoding)
print(request.text)
print(request.headers)
print(request.cookies)
print('-' * 100)
request.encoding = 'utf-8'
print(request.text)

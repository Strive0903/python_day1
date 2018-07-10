#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 导入requests包
#import requests

# get请求方法
#r = requests.get("http://www.baidu.com/")
# 各种请求方式
#r = requests.post("http://httpbin.org/post")

# requests 接受三个参数
#r = requests.get(url, params=None, **kwargs)
# 其中**kwargs包括如下：
'''
headers : 字典，HTTP定制头

cookies : 字典或CookieJar，Request中的cookie

auth : 元组，支持HTTP认证功能

files : 字典类型，传输文件

timeout : 设定超时时间，秒为单位

proxies : 字典类型，设定访问代理服务器，可以增加登录认证

allow_redirects : True/False，默认为True，重定向开关

stream : True/False，默认为True，获取内容立即下载开关

verify : True/False，默认为True，认证SSL证书开关

cert : 本地SSL证书路径

url: 拟更新页面的url链接

data: 字典、字节序列或文件，Request的内容

json: JSON格式的数据，Request的内容
'''

# 两个常用的控制参数 headers 和 proxies
# 添加headers 谷歌浏览器chrome://version
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
# }
# r = requests.get("https://www.zhihu.com",headers=headers)

# 自定义代理池
# import requests
# proxy = {
#     "http": "http://user:pass@10.10.10.1:1234",
#     "https": "https://10.10.10.1:4321"
# }
# r = requests.get('http://www.baidu.com',proxies=proxy)

# 增加延迟 timeout
# r = requests.get("https://book.douban.com/subject/1084336/comments/", timeout=20)
# print(r.status_code)

# 传递URL参数
#url = 'http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg'
#params = {'ie' : 'UTF-8', 'wd' : 'github'}
#r = requests.get(url ,params=params)
#print(r.url)

# 保存图片到本地
# r = requests.get(url, timeout=20)
# b = r.content
# # 本地路径左斜线
# with open("C:/Users/Public/Pictures/a.jpg",'wb') as f:
#     f.write(b)


# 打印cookie信息
#print(r.cookies)
# 编码 utf-8 ISO-8859-1
# print(r.encoding) #从header中猜测的响应编码形成
# print(r.apparent_encoding) #响应内容的实际编码形式
# # 类型
# print(type(r))
# # 输出文本内容
# #print(r.text)
# # 输出状态码 200表示成功
# print(r.status_code)
# 输出二进制
#print(r.content)
# 转换为utf-8
#print(r.content.decode('utf-8'))


# 简单的爬虫框架
'''
定义函数    #通用爬虫 有很多模块，行使不同的功能，
设置超时    #爬行多个网页，设置超时等待
异常处理    #使用try...except捕获异常
调用函数
'''
import requests

def getHTML.Text(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status() #失败请求，如果响应码非200，会抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHTML.Text(url))


# import requests
# from requests.exceptions import ReadTimeout,HTTPError,RequestException
#
# try:
#     r = requests.get("http://www.baidu.com",timeout=1)
#     print(r.status_code)
#     print(r.encoding)#ISO-8859-1
#     print(r.apparent_encoding)#utf-8
#     print(r.text)
#     r.encoding = r.apparent_encoding#修改编码
#     print(r.text)
# except ReadTimeout:
#     print('timeout')
# except HTTPError:
#     print('httperror')
# except RequestException:
#     print('reqerror')
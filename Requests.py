#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 导入requests包
import requests

# get请求方法
#r = requests.get("http://www.baidu.com/")
# 各种请求方式
#r = requests.post("http://httpbin.org/post")

# requests 接受三个参数
#r = requests.get(url, params=None, **kwargs)
# 其中**kwargs包括如下：
# headers:字典，HTTP定制头

# 添加headers 谷歌浏览器chrome://version
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
r = requests.get("https://www.zhihu.com",headers=headers)


# 传递URL参数
#url = 'http://www.baidu.com/s'
#params = {'ie' : 'UTF-8', 'wd' : 'github'}
#r = requests.get(url ,params=params)
#print(r.url)


# json
#print(r.json)
# 编码 utf-8 ISO-8859-1
print(r.encoding)
# 类型
print(type(r))
# 输出文本内容
#print(r.text)
# 输出状态码 200表示成功
print(r.status_code)
# 输出二进制
#print(r.content)
# 转换为utf-8
#print(r.content.decode('utf-8'))



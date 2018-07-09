#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 导入requests包
import requests
# get请求方法
r = requests.get("http://www.baidu.com/")
# requests 接受三个参数
#r = requests.get(url, params=None, **kwargs)
# 其中**kwargs包括如下：
# headers:字典，HTTP定制头




# 传递URL参数
#url = 'http://www.baidu.com/s'
#params = {'ie' : 'UTF-8', 'wd' : 'github'}
#r = requests.get(url ,params=params)
#print(r.url)

# 编码
print(r.encoding)
print(r.text)
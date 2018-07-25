#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
import requests
import pandas as pd
import numpy as np


url = "https://book.douban.com/subject/1084336/comments/"

df = pd.DataFrame(np.random.randn(6,3))
print(df.head())
df.to_csv("nummpy.csv")

'''

'''
爬虫三步走
'''
import requests
from lxml import etree
import pandas as pd

# 获取数据
url = "https://book.douban.com/subject/1084336/comments/"
r = requests.get(url).text
#print(r.text)

# 解析数据
s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')

# 保存数据
df = pd.DataFrame(file)
print(df.head)
df.to_csv("/Users/Young/Desktop/DuanPin.csv",'w')


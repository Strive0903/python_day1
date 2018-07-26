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

'''
import requests
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
#for item in pattern:
#    print(item.string)
import pandas
comments = []
for item in pattern:
    comments.append(item.get_text())
df = pandas.DataFrame(comments)
df.to_csv('comments.csv', encoding = "utf_8_sig")
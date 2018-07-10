#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
爬虫入门到精通-网页的解析（xpath）https://zhuanlan.zhihu.com/p/25572729
requests获取数据，xpath解析数据，pandas保存数据
'''

import requests
from lxml import etree

# 定义一个函数，给它一个html,返回xml
def getxpath(html):
    return etree.HTML(html)

# 提供一个案例html
html = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""
'''
# 获取xml结构
s = getxpath(html)
print(type(s)) #<class 'lxml.etree._Element'>
# 获取文本
print(s.xpath('//title/text()')) #['My page']
print(s.xpath('//body/text()'))
print(s.xpath('//head/text()'))
print(s.xpath('//html/head/title/text()')) #['My page']
print(s.xpath('//body/p/text()')) #['This is the first paragraph.']
print(s.xpath('body/p/text()')) #['This is the first paragraph.']
print(s.xpath('//p/text()')) #['This is the first paragraph.']
print(s.xpath('//h2/text()')) #['Welcome to my ']
print(s.xpath('//a/text()')) #['page']

# 获取属性的值
print(s.xpath('//h2/a/@href')) # ['#']
print(s.xpath('//h2/a/@src')) # ['x']
print(s.xpath('//@href'))
print(s.xpath('//@src'))

# 获取所有文本
print(s.xpath('//text()'))
# 获取所有注释
print(s.xpath('//comment()'))
'''

sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""
s2 = getxpath(sample2)

# 输出所有的li
print(s2.xpath('//li/text()')) # ['Quote 1', 'Quote 2 with ', 'Quote 3 with ', ' ...']
# 输出第一个li
print(s2.xpath('//li[1]/text()')) #['Quote 1']
print(s2.xpath('//li[position()=1]/text()')) #['Quote 1']
# 输出第二个li
print(s2.xpath('//li[2]/text()')) #
print(s2.xpath('//li[position()=2]/text()')) #['Quote 2 with ']
# 输出li下面有a的
print(s2.xpath('//li[a]/text()')) # ['Quote 2 with ', 'Quote 3 with ']
# 输出li下面有h2或a
print(s2.xpath('//li[a or h2]/text()')) # ['Quote 2 with ', 'Quote 3 with ', ' ...']
# 输出a和h2
print(s2.xpath('//a/text()|//h2/text()')) # ['link', 'another link', 'Quote 4 title']



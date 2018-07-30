#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
选择器 例子  例子描述
.class .top 选择class="top"的所有元素
#id #li_a_div   选择id="li_a_div"的所有元素
*   *   选择所有元素
element p 选择<p>元素
element,element li,div  选择所有<li>元素和所有<div>元素
element element li div  选择<li>元素内部的所有<div>元素
element>element li>div  选择父元素为<div>元素的所有<p>元素

'''

# 练习1 CSS选择器
from scrapy import Selector

# 打开同级目录下的HTML文件，所获取的sel变量是Selector变量，可以直接用sel.css（）对其进行选择
with open('test.html', encoding='utf-8') as f:
    text = f.read()

sel = Selector(text=text)
#print(isinstance('sel',Selector)) #Fasle
#print(type(sel)) # <class 'scrapy.selector.unified.Selector'>

# 选择class="top"的元素：
print(sel.css(".top"))
print(type(sel.css(".top"))) # 返回SelectorList实例



# 选择id="li_a_div"的元素：
print(sel.css("#li_a_div"))

# 选择所有元素：
print(sel.css("*"))

# 选择li元素内部的所有div的元素
print(sel.css("li div"))

# 选择父元素为li元素的所有div元素：
print(sel.css('li > div'))
# 调用.extract()方法,提取数据
print(sel.css('li > div').extract())
print(sel.css('li > div').extract_first())

# 选择所有的div元素和所有的li元素：
print(sel.css("li,div")) #与li div区别？
print(sel.css("li,div").extract())
print(sel.css("li,div").extract_first())


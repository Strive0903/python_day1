#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
爬虫的知识体系
1、前端html,css,js,浏览器相关知识
2、各种数据库的运用
3、http协议的了解
4、对于前后台联动的方案

爬虫进阶的工作流程：合适的组件做合适的事情
scrapy重要组件
1.Scrapy Engine引擎 2.Scheduler调度器 3.Downloader下载器
4.Spiders蜘蛛 5.Item Pipelines项目管道 6.Downloader Middlewares下载器中间件 7.Spider Middlewares蜘蛛中间件
下载中间件：第一步校验设计各种反爬+设计各种防范机制
蜘蛛中间件：第二步校验已处理完数据判断
项目管道：拦截，清洗校验储存数据
--return item或抛出异常

基本操作：
1、scrapy startproject city58
2、cd city58
3、scrapy genspider city58_test 58.com # 爬虫名称与项目名称不同


组件爬虫介绍：
1、name属性，不可重复，决定scrapy启动哪个爬虫
2、首先，从start_urls里面读取链接
     然后，自动调用start_requests函数
     最后，从函数请求的结果自动调用默认解析器parse
3、启动方法start_requests(),重写方法，是否放弃 start_urls；如果不写回调函数，默认用parse

'''
'''
迭代器

作用：访问集合元素的一种方式；
特点：
1、迭代器是一个可以记住遍历的位置的对象
2、迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器不能后退
3、迭代器有两个基本方法，iter()和next()
4、字符串、列表或元组对象都可用于创建迭代器
'''

list = [1, 2, 3, 4]
it = iter(list) # 创建迭代器对象
print(next(it)) # 输出迭代器的下一个元素 1
print(next(it)) # 输出2

'''
生成器
原理：在for循环过程中不断计算下一个元素，并在适当条件结束for循环
作用：对延迟操作提供了支持。所谓延迟操作，指在需要的时候才产生结果，而不是立即产生结果
Python有两种不同的方式提供生成器：
1、生成器函数：常规函数定义，使用yield语句而不是return语句返回结果，yield语句一次返回一个结果，在每个结果中间，挂起函数状态，
以便下次从它离开的地方继续执行
2、生成器表达式：类似于列表推导，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

获取生成器结果：
1、next（）基本不会用到
2、for循环 基本是这

学习网址：https://blog.csdn.net/qq_35976351/article/details/79680121
'''

# 生成器表达式：
squares = [x**2 for x in range(5)] # 列表生成式
print(squares) #[0, 1, 4, 9, 16]

squares2 = (x**2 for x in range(5)) #生成器表达式
print(squares2) # 生成器对象 <generator object <genexpr> at 0x10a8e14c0>
# for循环
print(next(squares2))
print("for循环如下:")
for n in squares2:
    print(n)

'''
在调用生成器函数运行过程中，每次遇到yield时函数在此处中断，返回yield的值。并在下一次从当前位置继续执行
'''
def mygenerator():
    print("start...")
    yield 5

g1 = mygenerator()
print(g1) # 此处调用，并没有打印start...，说明存在yield为生成器函数，没有运行
print(next(mygenerator())) # 调用next()即可输出

# 函数中有多个yield
def fun2():
    print('first')
    yield 10
    print('second')
    yield 20
    print('end...')

g2 = fun2()
#print(next(g2))
#print("for循环")
for b in g2:
    print(b)


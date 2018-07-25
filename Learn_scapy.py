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

'''




#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
mac端启动 brew services start mongodb@3.4
mac端停止 brew services stop mongodb@3.4
mongodb使用：启动client-创建数据库-创建数据集-写入数据
'''

from pymongo import MongoClient

client = MongoClient()
db = client.test # 连接test数据库，没有则自动创建
my_set = db.set # 使用set集合，没有则自动创建

my_set.insert({"name":"yyy","age":18}) # 写入字典数据
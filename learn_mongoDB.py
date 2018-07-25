#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
mac端启动 brew services start mongodb@3.4
mac端停止 brew services stop mongodb@3.4
mongodb使用：启动client-创建数据库-创建数据集-写入数据
创建连接MongoDB：
方法1：client = pymongo.MongoClient(host='localhost',port=27017)
方法2：client = MongoClient() #默认等价MongoClient('mongodb://localhost:27017/')
学习链接：https://www.cnblogs.com/nixingguo/p/7260604.html
'''

'''
from pymongo import MongoClient

# 连接MongoDB
client = MongoClient()
# 指定数据库
db = client.test # 连接test数据库，没有则自动创建
# 指定集合，即表
my_set = db.set # 使用set集合，没有则自动创建
# 插入数据
my_set.insert({"name":"yyy","age":18}) # 写入字典数据

# 插入单条
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = my_set.insert_one(srudent)
print(result)
print(result.inserted_id)

# 插入多条
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = my_set.insert_many([student1,student2])
print(result)
print(result.inserted_ids)

'''




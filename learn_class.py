#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
面向对象编程，类和对象
类是抽象的模板，对象是根据模板创建的，每个对象都有相同的方法，但有不同的数据

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
'''
'''
定义类:class+类名大写字母开头+（object）

class Student(object):
    pass
    
创建对象的时候，强制绑定一些属性，用__init__方法,方法第一个参数为self，表示对象本身，
有了__init__方法，在创建对象的时候必须传入匹配参数

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

类中定义函数和普通函数相比，只是第一个参数永远为实例变量self，调用时，不用传递参数
'''
'''
创建实例：类名+（）

zhangsan = Student()
可以自由给对象绑定属性
zhangsan.score = "98"
'''

# 数据封装：将数据保存某处，从某处调用数据；在类中定义访问数据的函数
class Student(object):
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def print_score(self):
        print("%s: %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节
young = Student('young',22,99)
lucy = Student('lucy',24,59)
print(young.age, young.get_grade())
print(lucy.age,lucy.get_grade())

# 对象直接调用方法
young.print_score() # young: 99


'''
class Person(object):
# 这里就是初始化将要创建实例对象的属性
    def __init__(self, high, weight, age):
        self.high = high
        self.weight = weight
        self.age = age

# 定义要创建实例对象的有用技能
    def paoniu(self):
        print("你拥有泡妞技能！")

    def eat(self):
        print("你能吃！")

# 开始创建实例
zhangsan = Person(180,70,20)
lisi = Person(170,65,18)

# 实例开始使用技能
zhangsan.paoniu()
lisi.eat()
'''
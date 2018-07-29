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
# 练习1
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
'''
# 练习2
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


'''
# 练习3
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

'''
面向对象编程，访问限制
作用：让Class内部属性不被外部访问
方式：把属性的名称前加两个下划线__，在python中，实例的变量名如果以__开头，就变成了一个私有变量
原因：有些私有变量不被直接修改，为了给私有变量设置修改条件，满足添加才被修改
'''
'''
# 练习4
# 请把下面Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        # gender创建为私有变量
        self.__gender = gender

    # 设置外部访问gender方法
    def get_gender(self):
        return self.__gender

    # 设置外部修改gender方法
    def set_gender(self, gender):
        # 外部参数gender为male才能修改
        if gender == 'male':
            self.__gender = gender
        else:
            raise ValueError('error gender')

young = Student('lucy', 'male')
print(young.name)
# 外部无法访问到gender
#print(young.gender)
print(young.get_gender())

# 外部可直接修改name属性,无法修改gender属性
young.name = 'bili'
print(young.name)
young.gender = 'woman'
print(young.gender) # 输出woman
print(young._Student__gender) # 输出man
young.set_gender('male')
print(young.get_gender())
young.set_gender('female')
print(young.get_gender())

'''

'''
继承：新的class称为子类(Subclass), 而被继承的class称为基类、父类或超类（Base class、 Superl class）
作用：子类获得了父类的全部功能, 子类可以把父类不适合的方法重写，新增子类特有的方法
'''
# 练习5

# 定义Animal类
class Animal(object):

    def run(self):
        print('Animal is running...')

# Dog 和 Cat类继承Animal类,只继承不做处理

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Dog 和 Cat获得了父类的全部功能
dog = Dog()
print(dog.run())
cat = Cat()
print(cat.run())

# 继承之后可以对代码改进，子类方法覆盖父类方法

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

dog = Dog()
print(dog.run())
cat = Cat()
print(cat.run())

'''
多态：数据类型一致下，子类都可调用定义的父类方法
作用：鸭子模型，灵活
'''

# 定义函数，变量为父类实例对象，
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Dog()))
print(run_twice(Animal()))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'


# 多重继承
class Animal(object):
    pass

# 哺乳动物
class Mammal(Animal):
    pass

# 鸟
class Bird(object):
    pass

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。


class RunnableMixIn(object):
    def run(self):
        print('running...')

class FlyableMixIn(object):
    def fly(self):
        print('flying...')


# 狗是哺乳动物
class Dog(Mammal, RunnableMixIn):
    pass

# 蝙蝠是哺乳动物
class Bat(Mammal, FlyableMixIn):
    pass

# 鹦鹉
class Parrot(Bird):
    pass

# 鸵鸟
class Ostrich(Bird):
    pass



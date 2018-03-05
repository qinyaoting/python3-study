#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

import math

__author__ = 'chin'

def power(x):
    return x*x

def adv_power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def adv_power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_L(L = []):
    L.append('END')
    return L

def add_LL(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i

    return sum




if __name__ == '__main__':

    # 位置参数
    # 计算5的平方
    print(power(5))

    # 计算n的m次方 adv_power(x, n) x n都是位置参数
    print(adv_power(2,3))
    print(adv_power(5,0))
    print(adv_power(5,2))
    print(adv_power(5,3))

    # 默认参数
    print(adv_power2(5))
    print(adv_power2(5, 3))

    # 默认参数错误使用例子
    print(add_L(['1','2','3','4']))
    print(add_L(['x','y','z','o']))

    print(add_L())
    print(add_L())
    # Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

    # 注意: 默认参数必须指向不变对象

    print(add_LL())
    print(add_LL())
    print(add_LL())

    # 可变参数
    # def func(*argum):
    print(calc(1,2,3,4))
    print(calc())

    num = [1,2,3]
    print(calc(num[0], num[1], num[2])) # 太笨的办法
    print(calc(*num)) # 奇特 把list前边添加一个星号, 变为tuple, 传给方法


    # 关键字参数
    # 参数名称前用两个星号表示为关键字参数
    def person(name, age, **kw):
        print('name',name, 'age',age, 'othter',kw)

    print(person('tom', 22))
    print(person('bob', 35, city='bj'))
    print(person('lucy', 25, gender='F', job='engineer'))

    extra = {'gender':'M','job':'agent'}
    person('jack', 55, **extra)
    # 注意:**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

    # 命名关键字参数 city和job是命名关键字参数
    def person(name, age, *, city, job):
        print(name, age, city, job)


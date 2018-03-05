#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

import math

__author__ = 'chin'

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    # 奇特: 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号
    return nx, ny

if __name__ == '__main__':

    # 定义函数
    print(my_abs(-11))
    print(my_abs(11))
    # 如果参数个数不对, 会抛出 TypeError: my_abs() takes 1 positional argument but 2 were given
    #print(my_abs(11, 22))

    # 如果参数类型不对 TypeError: '>=' not supported between instances of 'str' and 'int'
    # print(my_abs('A'))

    # 奇特: 返回多个值
    x, y = move(100, 100, 60, math.pi/6)
    print(x, y)





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

__author__ = 'chin'

if __name__ == '__main__':

    # 调用函数
    print(abs(100))
    print(abs(-1))
    print(abs(12.06))

    # 如果传入参数类型不对, 会报TypeError的错误
    # print(abs(1,2 )) # TypeError: abs() takes exactly one argument (2 given)
    # print(abs('a')) #bad operand type for abs()

    #max(), 可以传递任意多个参数, 返回最大的值
    print(max(3,4,5))
    print(max(6.1,4.1,4.5))

    # 数据类型转换
    print(int('123'))
    # print(int('123.5')) 不能直接转
    print(int(12.34))
    print(int(12.98))
    print(float('12.34'))
    print(str(123))
    print(str(123.45))
    print(bool(1))
    print(bool(''))

    # 奇特: 可以吧函数付给一个变量, 就像给函数起了个别名
    # 要转变思路, 吧函数当成变量, 肯定有它的好处
    a = abs
    print(a(-111))

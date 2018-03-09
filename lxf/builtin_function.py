#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

__author__ = 'chin'

if __name__ == '__main__':

    # enumerate(iterable, start=0)
    '''
    Return an enumerate object. iterable must be a sequence, an iterator, 
    or some other object which supports iteration. The __next__() method of 
    the iterator returned by enumerate() returns a tuple containing a count 
    (from start which defaults to 0) and the values obtained from iterating over iterable.
    
    返回一个枚举对象, 传入的迭代参数必须是一个序列, 或者一个迭代器, 
    或者支持迭代的其他对象. 迭代器的__next()__方法(由enumerate()方法返回)返回一个tuple, tuple包含
    一个计数和一个值, 值是迭代参数迭代出来的.
    '''

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))
    print(list(enumerate(seasons, start=1)))

    # 等同于下边方法
    # def enumerate(sequence, start=0):
    #     n = start
    #     for elem in sequence:
    #         yield n, elem
    #         n += 1

    for (c, item) in enumerate(seasons):
        print(c, item)


    # tuple
    print(tuple('abc'))
    print(tuple([1, 2, 3]))


    # glob
    import glob
    # 查找当前目录下txt文件
    print(glob.glob('*.txt'))
    # 查找当前目录及子目录下的txt文件
    print(glob.glob('**/*.txt', recursive=True))


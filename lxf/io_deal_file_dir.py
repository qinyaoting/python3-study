#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from os import read

__author__ = 'chin'

# 操作文件和目录



if __name__ == '__main__':
    import os

    # 操作系统类型, posix 是linux 如果是nt就是windows
    print(os.name)

    # 系统信息详细内容
    print(os.uname())

    # 环境变量
    print(os.environ)

    # 获得环境变量的某个值
    print(os.environ.get('PATH'))
    print(os.environ.get('x', 'default'))

    # 操作文件和目录

    # 获得当前的绝对路径
    print(os.path.abspath('.'))

    print(os.path.join('.','testdir'))

    # 创建目录
    os.mkdir('./testdir')
    # 删除目录
    os.rmdir('./testdir')

    # split会把文件名和前边地址拆分开
    print(os.path.split('./testdir/ttt.txt'))
    # 可以得到文件的扩展名称(但是包括点)
    print(os.path.splitext('./testdir/ttt.txt'))

    with open('./test.txt','w') as f:
        f.write('Hello........')
    os.rename('test.txt', 'test.py')
    os.remove('test.py')

    # 列出全部目录
    os.mkdir('./testdir')
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    os.rmdir('./testdir')

    # 列出.py结尾的文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


    # 如果目录不存在就创建
    # if the output directory does not exist, create it
    save_path = './test_images'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 用字典实现计数
    counts = {}
    letter = 'a'
    for i in range(10):
        count = counts.get(letter, 1)
        counts[letter] = count+1


    # zfill(6), 往前补0
    i = 1
    p = os.path.join(save_path, '{}.png'.format(str(i).zfill(6)))
    print(p)


    # zip 可以同时遍历
    for li, ch in zip([(1,1,1,),(2,2,2),(3,3,3)], 'XYZ'):
        print(li, ch)


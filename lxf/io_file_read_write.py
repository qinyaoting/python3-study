#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from os import read

__author__ = 'chin'

# 读文件

if __name__ == '__main__':
    # 笨办法1
    # 'r' 表示只读, 'w'表示写, read()方法返回文件的全部内容,如果是大文件,请勿使用
    f = open('./testio.txt','r')
    print(f.read())
    # close()是关闭文件
    f.close()


    # 笨办法2
    try:
        f2 = open('./testio.txt', 'r')
        print(f2.read())
    finally:
        if f2:
            f2.close()

    # 机灵办法1, 好处是不必再调用close()方法了
    with open('./testio.txt', 'r') as f:
        print(f.read())

    # 未避免read()方法, 读到大文件撑爆内存, 可以使用read(size)方法,每次读size个字节的内容
    # readlines()每次读取一行内容
    with open('./testio.txt', 'r') as f:
        for line in f.readlines():
            print("=============")
            print(line.strip())

    # 如果是图片或者视频, 打开文件的模式就需要为'rb', 以二进制文件的方式
    with open('./testio_googlelogo.png', 'rb') as f:
        print(f.read())


    # 读取飞utf-8编码的文本文件, 可以指定编码类型
    with open('./testio.txt', 'r',encoding='gbk') as f:
        print(f.read())

    # 某些文件夹杂了非法的编码, 可以指定参数忽略它,
    with open('./testio.txt', 'r', encoding='gbk', errors='ignore') as f:
        print(f.read())


    # 写文件
    # 'w'写模式, 覆盖  'wb'以二进制方式写模式
    with open('./text_write.txt', 'w') as f:
        print(f.write('tomcat ......1'))

    # 'a'表示追加模式
    with open('./test_write_append.txt', 'a') as f:
        print(f.write('gogogo....'))

    # 指定编码
    with open('./test_write_encoding.txt', 'a', encoding='gbk') as f:
        print(f.write('666老铁----\n'))

    f6 = open('./test_write_encoding.txt','r')
    print(f6.encoding)
    f6.close()

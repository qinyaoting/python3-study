#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

import sys

# 标准


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello, world!")
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

# 作用域
# 以下横线开头的变量是非公开变量, 如__name__ _abc, 不要在外部引用

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
斐波那契数列
这个数列从第3项开始，每一项都等于前两项之和
'''


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(1000)

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


'''
'''

fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

print(list(enumerate(fruits)))
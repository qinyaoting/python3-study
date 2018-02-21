#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

# 使用元类

class Hello(object):
    def hello(self, name='Tom'):
        print('Hello %s' % name)


if __name__ == '__main__':
    h = Hello()
    print(h.hello('Jack'))
    print(type(Hello))
    print(type(h))


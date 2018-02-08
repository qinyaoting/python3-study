#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

# 类中定义函数, 函数第一个参数总是self,代表实体本身

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    bob = Student('Bob', 75)
    print(bob.get_grade())
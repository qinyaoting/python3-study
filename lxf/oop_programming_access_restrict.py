#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

# 类中定义函数, 函数第一个参数总是self,代表实体本身

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')


if __name__ == '__main__':
    bob = Student('Bob', 75)
    print(bob.get_grade())
    bob.print_score()
    # bob.__name ## AttributeError: 'Student' object has no attribute '__name'
    # bob._Student__name
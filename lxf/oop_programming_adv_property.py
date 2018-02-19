#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    # def get_score(self):
    #     return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('Score must be an integer')
    #     if value <0 or value > 100:
    #         raise ValueError('score must between 0-100')
    #     self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value <0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value


if __name__ == '__main__':
    s = Student()
    s.score = 60
    s.score

    # s.set_score(9999)

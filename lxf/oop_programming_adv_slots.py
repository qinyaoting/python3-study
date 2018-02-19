#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'


class Student(object):
    pass


class GraduateStudent(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称 仅对当前类实例起作用，对继承的子类是不起作用的：

if __name__ == '__main__':
    s = Student()
    # 动态给实例绑定一个属性
    s.name = 'Bob'
    print(s.name)

    # # 给实例绑定一个方法
    def set_age(self, age):
        self.age = age

    from types import MethodType
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)

    s2 = Student()
    # 不行 s2.set_age(25)

    # 给class绑定方法
    def set_score(self, score):
        self.score = score

    Student.set_score = set_score
    s.set_score(100)
    s2.set_score(2000)

    s3 = GraduateStudent()
    s3.name = 'tom'
    s3.age = 19


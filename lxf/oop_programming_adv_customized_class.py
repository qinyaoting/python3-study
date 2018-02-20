#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'


# 定制类

# __str__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student name is %s' % self.name

    def __call__(self, *args, **kwargs):
        print('my name is %s' % self.name)

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a, b = b, a+b
        return a

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

# __call__
# __getattr__


if __name__ == '__main__':
    s = Student('Tom')
    print(s)
    for i in Fib():
        print(i)
    f = Fib()
    print(f[0])
    print(f[2])

    # 正常的调用是instance.method()， python可以在实例本身调用， 但需要在类中覆盖__call__()方法
    s()

    # 判断一个实例能否被调用， 使用callable(instance)
    print(callable(Student('Bob')))
    print(callable(max))
    print(callable([1,2,3]))
    print(callable(None))
    print(callable('str'))


#!/usr/bin/python3

# 获取对象信息

# 用type()来判断对象类型
from lxf.oop_programming_inherit import Dog

print(type(123))
print(type('ABC'))
print(type(None))

# 判断方法, 判断类
print(type(abs))
a = Dog()
print(type(a))

#
print(type(123) == type(456))
print(type(123) == int)
print(type('ABC') == str)
print(type('ABC') == type(123))

# 基本数据类型可以直接写int str, 要判断一个对象是否是函数怎么办?可以使用types

import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

# 判断一个变量是否是某些类型中的一种
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))

#dir()
# 获得一个str对象的所有属性和方法
print(dir('ABC'))

# getattr()、setattr()以及hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
# print(getattr(obj, 'z')) AttributeError: 'MyObject' object has no attribute 'z'
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())

# 一个正确的用法的例子如下
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
def readData(fp):
    pass

#!/usr/bin/python3

# map reduce


# map第一个参数是一个方法, 第二个参数是一个Iterator,
# 可以作用于for循环的对象都是Iterable, 作用于next()函数的对象都是Iterator(表示一个惰性计算的序列)o
# list,dict, str是Iterable而不是Iterator, 可以通过iter()转换为Iterator对象
def f(x):
    return x*x

r = map(f, range(1,10))
# for x in r:
#     print(x, end=' ')

print(list(r))

# 把list的数字转为字符串

r = map(str, [1,2,3,4,5,6])
print(list(r))

# reduce
from functools import reduce
def add(x, y):
    return x+y

print(reduce(add, [1,3,5,7,9]))



def fn(x, y):
    return x*10 + y

print(reduce(fn, [1,3,5,7,9]))


DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8, '9':9}
def ch2num(s):
    return DIGITS[s]

print(reduce(fn, map(ch2num, '12379')))

#!/usr/bin/python3

# filter

# filter第一个参数是方法, 第二个序列中的每一个元素都会调用方法, 方法返回True或者false,


# 删除序列中的偶数
def is_odd(s):
    return s % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))


# 删除序列中的空字符串
str1 = ['A','B',' ', None, 'C']
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, str1)))
# ['A', 'B', 'C']
# filter()函数返回的是一个Iterator，也就是一个惰性序列，要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


# 构造一个从3开始的基数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定一个筛选算法
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 计算素数的一个方法是埃氏筛法，
for n in primes():
    if n < 1000:
        print(n, end=' ')
    else:
        break

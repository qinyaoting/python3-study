#!/usr/bin/python3

# 高阶函数

# 可以把函数赋给变量, 奇特
d = abs

print(abs(-11))
print(d(-21))

# 变量可以指向函数, 函数的参数能接受变量, 一个函数可以接收另一个函数作为参数, 这种函数就是高阶函数


# 简单的高阶函数
def add(a, b, fn):
    return fn(a) + fn(b)

# 计算-5绝对值加6的绝对值等于几
print(add(-5, 6, abs))

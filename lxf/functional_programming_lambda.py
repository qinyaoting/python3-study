#!/usr/bin/python3

# 匿名函数就是lambda

# 冒号前的x表示的是输入参数, 冒号后的是计算逻辑
print(list(map(lambda x:x*x, [1,2,3,4,5])))

# lambda函数的限制只能有一个表达式, 不能有return

def build(x, y):
    return lambda: x*x + y*y

# build(3,4)是不能获得结果的
print(build(3,4))

# 记住: 因为返回的是给匿名函数,如果要计算结果,再加()
print(build(3,4)())


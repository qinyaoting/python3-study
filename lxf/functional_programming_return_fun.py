#!/usr/bin/python3

# 返回函数

# 可以在函数内部定义一个新的函数, 将该函数返回

# 可变参数的求和
# 通常的定义方法
import types


def calc_sum(*args):
    ax = 0
    for num in args:
       ax = ax + num
    return ax

# 奇特的定义方法, 好处是什么???
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum  # 返回的函数不带括号, 注意了

f = lazy_sum(1,3,5,7,9)
print(isinstance(f, types.FunctionType))

# 只有调用f(),才真正计算求和结果
print(f())


f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

print(f1 == f2)


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

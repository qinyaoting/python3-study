#!/usr/bin/python3

# 输入Hello, World字符串
print("Hello, World")

# 打印两位小数
print("%.3f" % 3.1415)

# 打印两位整数, 不足位数补零
print('%2d-%02d' % (3, 1))

# 可变参数 第二个参数默认是2 , 可以不传
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

# 传两个参数5的3次方
print(power(5, 3))

# 如果只传一个参数, 也是可以的
print(power(5))

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

# 可以吧list传给方法
print(calc([1,2,3]))

# 可以把tuple传给方法
print(calc((1,3,5,7)))

# 加个星号, 就变成可变参数了
def calc_with_alterable_params(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +  n*n
    return sum

print(calc_with_alterable_params(1, 2))
print(calc_with_alterable_params())
num = [1,2,3]
print(calc_with_alterable_params(num[0], num[1], num[2]))

# 把list传给方法, 星号的作用是把list变为可变参数传进去
print(calc_with_alterable_params(*num))






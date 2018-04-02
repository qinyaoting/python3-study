import numpy as np


a = np.array([10,20,30,40])
b = np.arange(4)

print(a, b)
c = a-b
print(c)

d= a+b
print(d)

e = a*b
print(e)


print(b**2)

f = np.sin(a)
print(f)

print(b)
print(b<3)


x = np.array([
    [1,1],
    [0,1]
])

y = np.arange(4).reshape((2,2))
print(x)
print(y)

# 矩阵乘法
# 单个元素对应相乘
z = x * y
print(z)
# 矩阵相乘, 一行乘一列
c_dot = np.dot(x, y)
print(c_dot)

c_dot2 = x.dot(y)
print(c_dot2)

# 小于1随机的矩阵, 2行4列
f1 = np.random.random((2,4))
print(f1)

# axis 0是列上运算, axis是1在行上
print(np.sum(f1, axis=1))
print(np.min(f1))
print(np.max(f1))
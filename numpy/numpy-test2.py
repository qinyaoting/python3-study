import numpy as np


a = np.array([
    [10, 20, 30, 40],
    [10, 20, 30, 40]])
b = np.arange(4)

print(a, b)
# 注意2, a,b能减, 要求列数相同
c = a-b
# print(c)

d = a+b
# print(d)

e = a*b
# print(e)

# **2作用在b的每个元素上
# print(b**2)

f = np.sin(a)
# print(f)

# 判断b中元素是否小于3, 是True, 否False, 返回list
print(b)
print(b < 3)

# 通过np array 和range来构造矩阵
x = np.array([
    [1, 1],
    [0, 1]
])
y = np.arange(4).reshape((2, 2))
print(x)
print(y)

# 矩阵乘法
# 单个元素对应相乘
z = x * y
# print(z)

# 矩阵相乘, 一行乘一列
c_dot = np.dot(x, y)
# print(c_dot)

c_dot2 = x.dot(y)
# print(c_dot2)

# 小于1随机的矩阵, 2行4列 注意3, 可以用np的random生成矩阵
f1 = np.random.random((2, 4))
print(f1)

# axis 0是列上运算, axis是1在行上
# print(np.sum(f1, axis=0))
print(np.min(f1))
print(np.max(f1))
print(np.mean(f1))

# 减去平均值
f1 -= np.mean(f1)
print(f1)

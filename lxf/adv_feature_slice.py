#!/usr/bin/python3

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 笨办法取前3个元素
print(L[0], L[1], L[2])

# 取前N个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 切片（Slice）操作符
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

# 创建一个0-99的数列
L2 = list(range(100))
print(L2)

# 前10个数
print(L2[:10])
# 后10个数
print(L2[-10:])
# 前11-20个数
print(L2[10:20])
# 前10个数， 每两个取一个
print(L2[:10:2])
# 所有数，每5个取一个
print(L2[::5])

print(L2[:])

# tuple
print((1,2,3,4,5)[:3])

# str
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

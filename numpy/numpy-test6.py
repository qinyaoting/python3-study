import numpy as np


'''
分割range
'''

a = np.arange(12).reshape((3,4))
print(a)

# 横向分割为两个矩阵
print(np.split(a,2, axis=1))

# 横向分割为3部分
print(np.split(a,3, axis=0))

# 不等量分割,
print(np.array_split(a, 3, axis=1))
print(np.vsplit(a, 3))
print(np.hsplit(a, 2))

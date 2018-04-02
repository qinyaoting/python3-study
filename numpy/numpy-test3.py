import numpy as np

'''
numpy的一些常用函数
'''

a = np.arange(2,14).reshape((3,4))
print(a)

# 最大最小索引
print(np.argmin(a))
print(np.argmax(a))

# 平均值
print(np.mean(a))
print(np.average(a))

# 中位数
print(np.median(a))

# 累加前边元素的矩阵
print(a)
print(np.cumsum(a))

#???
print(np.nonzero(a))

# 排序
print(np.sort(a))

# 行列互换
print(np.transpose(a))

# 小于5的变为5, 大于9的变为9, 其余不变
print(np.clip(a, 5, 9))

# 对列运算axis=0, axis=1对行计算
print(a)
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

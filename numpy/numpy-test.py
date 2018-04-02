import numpy as np

array = np.array([[1,2,3], [2,3,4]])

print(array)
# 数组是几维的
print('number of dim', array.ndim)
# 几行几列
print(array.shape)
# 共几个元素
print(array.size)




# 指定元素类型
a = np.array([2,3,4], dtype=np.int)
print(a) # 不是逗号分割
print(a.dtype)

# dtype=np.float

# 二维矩阵
a2 = np.array([
    [2,3,4],
    [5,6,7]
])

print(a2)

# 生成全是0的矩阵, 3行4列
a3 = np.zeros((3,4))
print(a3)

# 全是1
a4 = np.ones((3,4), dtype=int)
print(a4)

# 元素接近于0
a5 = np.empty((3,4))
print(a5)

# 10 到19 ,步长是2
a6 = np.arange(10, 20, 2)
print(a6)

# 范围构造矩阵
a7 = np.arange(12).reshape((3,4))
print(a7)

# 1到10, 的范围, 分为5段
a8 = np.linspace(1, 10, 5)
print(a8)

# 分为6段, 构造2行3列的矩阵
a9 = np.linspace(1, 10, 6).reshape((2,3))
print(a9)
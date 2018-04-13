import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 二）归一化----将数据特征缩放至某一范围(scalingfeatures to a range)
# 从列上看, 把列元素同时缩小, 变成0,1区间
data = np.array([
    [1., -1., 2.],
    [2., 0., 0.],
    [0., 1., -1.]])
# print(data)

scaler_x = MinMaxScaler(feature_range=(0, 1))
scaled_x_data = scaler_x.fit_transform(data)
# print(scaled_x_data)


# newaxis np.newaxis 为 numpy.ndarray（多维数组）增加一个轴

a = np.array([1, 2, 3, 4, 5])
# print(a.shape)  # 是数组

# 数组
# print(a)
# 数组变成1行5列的矩阵
b = a[np.newaxis, :]
# print(b)
# 数组变成5行1列的矩阵
c = a[:, np.newaxis]
# print(c)
# print(a.shape)
# print(b.shape)
# print(c.shape)

# 返回商的整数部分, 抛弃余数
# print(13/3)
# print(13//3)


# 取第一列, 输出的是list
print(data[:, 0])
# 通过reshape(-1,1)变为3行一列的矩阵
print(data[:, 0].reshape(-1, 1))

# x是索引, y是值
for x, y in enumerate(['a', 'b', 'c', 'd']):
    print(x, '-', y)

# round 保留几位小数
print(round(12406.815, 2))


if __name__ == '__main__':
    li = np.array([['a','b','c','d','e','f','g']])
    print(li[:, 1:7])
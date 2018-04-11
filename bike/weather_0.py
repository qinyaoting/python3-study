import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
# % matplotlib inline
import warnings


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

a = np.array([1,2,3,4,5])
# print(a)
# print(a.shape)  # 是数组

b = a[np.newaxis, :]
c = a[:, np.newaxis]
# 数组是一维的
print(a)
# 在一维数组上增加维度, 变成1行5列
print(b)
# 在一维数组上增加维度, 变成5行1列
print(c)
print(a.shape)
print(b.shape)
print(c.shape)



# //返回商的整数部分, 抛弃余数
# print(13/3)
print(13//3)



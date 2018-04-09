import pandas as pd
import numpy as np

# pandas
# Series是系列, 变成一列
s = pd.Series([1, 3, 6, np.nan, 44, 1])
# print(s)

# date函数
dates = pd.date_range('20160101', periods=6)
# print(dates)

# DataFrame矩阵, 索引是日期, 列名是 a b c d
df = pd.DataFrame(np.random.random(),
                  index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)

# 0到11的3行4列的矩阵
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print('0到11的3行4列的矩阵\n %s'% df1)

# 字典构造dataframe, key是列名, value是单元格的值,
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)

# 输出每个元素的类型
# print(df2.dtypes)

# print('df2 的索引是:%s ' % df2.index)
# print('df2 的列名是:%s ' % df2.columns)

# 输出df2的值
# print(df2.values)
# print(df2.describe())
# print(df2.T)

# 按列索引降续
# print(df2.sort_index(axis=1, ascending=False))
# 按行索引降续
# print(df2.sort_index(axis=0, ascending=False))

# 根据E列的值排序
# print(df2.sort_values(by='E'))

# 注意1, 复制list中的元素
print([3] * 4)
import pandas as pd
import numpy as np

# 构造3行4列的dataframe
df = pd.DataFrame(np.random.randn(3, 4))
print(df)
# 标识行
print(df.index)
# 标识列
print(df.columns)
# 维度
print(df.shape)
# df的概要信息, 总数, 平均值, 最大最小值
# print(df.describe())


# print(df[0])    #df取第一列

# print(df[:2])   #df去前两行

# print(df.loc[0])    #取第一行(按索引取)


# print(df.iloc[2])   #取第3行

# print(df.iloc[1:3])     #取第2.3行

# print(df.iloc[0, 1])  # 取第一行, 第2列的元素

# print(df.iloc[:2, :3])

# print(df.iloc[[1, 2], [1, 3]])
#
import pandas as pd
import numpy as np


dates = pd.date_range('20130101', periods=6)
# 第一个参数定义矩阵的值, 第二个参数定义行名称, 第三个参数定义列名称
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

# 有0的行丢掉
# print(df.dropna(axis=0))
#
# print(df.dropna(axis=0, how = 'any'))
# print(df.dropna(axis=0, how = 'all'))
# print(df.dropna(axis=1))


print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull() == True))

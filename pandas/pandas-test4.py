import pandas as pd
import numpy as np


dates = pd.date_range('20130101', periods=6)
# 第一个参数定义矩阵的值, 第二个参数定义行名称, 第三个参数定义列名称
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])
# 修改1,2  2,3的值
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

# 有nan的行丢掉
# print(df.dropna(axis=0))
#
# print(df.dropna(axis=0, how='any'))

# 只有全是nan, 才去掉
# 把第一行, 全改成nan
# df.iloc[0, :] = np.nan
# print(df)
# print(df.dropna(axis=0, how='all'))

# axis表示全列是nan,就删掉
# print(df.dropna(axis=1))

# 用0填充nan
# print(df.fillna(value=0))
# 判断单元格是否是nan
# print(df.isnull())

# 判断是否有nan
# print(np.any(df.isnull()==True))

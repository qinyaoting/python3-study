import pandas as pd
import numpy as np

'''
如何修改矩阵中的值
如何增加一列
'''
dates = pd.date_range('20130101', periods=6)
# 第一个参数定义矩阵的值, 第二个参数定义行名称, 第三个参数定义列名称
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)

df.iloc[2,2] = 1111

print(df)

df.loc['20130101', 'B'] = 222
print(df)

# df[df.A > 4] = 0
df.B[df.A > 4] = 0
print(df)

df['F'] = np.nan
print(df)

df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(df)

import pandas as pd
import numpy as np


dates = pd.date_range('20130101', periods=6)
# 第一个参数定义矩阵的值, 第二个参数定义行名称, 第三个参数定义列名称
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)

# 选择某一列
#print(df['A'])
#print(df.A)

# 切片
# print(df[0:3])
# print(df['20130102':'20130104'])

# 选择某一行
# print(df.loc['20130102'])
# # 选择A B列
# print(df.loc[:,['A','B']])
# # 选择某一行后的全部, 只显示A B两列
# print(df.loc['20130102':,['A','B']])
#
# print(df.iloc[3])
# print(df.iloc[3,1])
# print(df.iloc[3:5,1:3])
# print(df.iloc[[1,3,5],1:3])

#print(df.ix[:3, ['A','C']])

print(df[df.A > 8])
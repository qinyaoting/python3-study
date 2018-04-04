import pandas as pd
import numpy as np

'''
如何修改矩阵中的值
'''
dates = pd.date_range('20130101', periods=6)
# 第一个参数定义矩阵的值, 第二个参数定义行名称, 第三个参数定义列名称
df = pd.DataFrame(
    np.arange(24).reshape((6, 4)),
    index=dates,
    columns=['A', 'B', 'C', 'D'])
print(df)

# 把第3行第3列的元素改为1111
df.iloc[2, 2] = 1111
# print(df)

# 根据索引,修改单元格的值
df.loc['20130101', 'B'] = 222
# print(df)

# A列元素值大于4的修改为0
# df[df.A > 4] = 0
# print(df)

# 只修改B列, 条件是A列元素大于4的
# df.B[df.A > 4] = 0
# print(df)

# 增加F列, 并赋值nan
df['F'] = np.nan
# print(df)

# 增加E列, 并赋值根据索引
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
# print(df)
#
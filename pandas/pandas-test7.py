import pandas as pd
import numpy as np


left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                     'B':['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                     'D':['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)


res = pd.merge(left, right, on='key')
print(res)

left1 = pd.DataFrame({
    'key1':['K0', 'K0', 'K1', 'K2'],
    'key2':['K0', 'K1', 'K0', 'K1'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                     'B':['B0', 'B1', 'B2', 'B3']})

right1 = pd.DataFrame({
    'key1':['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                     'D':['D0', 'D1', 'D2', 'D3']})
print(left1)
print(right1)

res = pd.merge(left1, right1, on=['key1', 'key2'], how='outer') # how = left|right|outer|inner
print(res)

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2], 'col_right':[2,2,2]})

print(df1)
print(df2)

# 提示合并方式
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# res = pd.merge(df1, df2, on='col1', how='outer', indicator="indicator_column")
res = pd.merge(df1, df2, on='col1', how='outer', indicator="indicator_column")

print(res)


df5 = pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

print(df5)

df6 = pd.DataFrame({
    'C':['C0','C2','C3'],
    'D':['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])

print(df6)
# 根据index, 合并df
# res = pd.merge(df5, df6, left_index=True, right_index=True, how='inner')
res = pd.merge(df5, df6, left_index=True, right_index=True, how='outer')
print(res)

boys = pd.DataFrame({
    'k':['K0', 'K1', 'K2'], 'age':[1,2,3]
})
girls = pd.DataFrame({
    'k':['K0', 'K2', 'K3'], 'age':[4,5,6]
})
print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)

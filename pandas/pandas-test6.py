import pandas as pd
import numpy as np

'''
合并dataframe
'''
# ones返回3行4列的矩阵, 元素都是1
# print(np.ones((3, 4)))

df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])


# print(df1)
# print(df2)
# print(df3)

# 上下合并
res = pd.concat([df1, df2, df3], axis=0)
# print(res)

# 重新索引
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)


# concat
df5 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df6 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df5)
print(df6)

# 并集合并
res2 = pd.concat([df5, df6], join='outer')
# print(res2)

# 交集合并
res2 = pd.concat([df5, df6], join='inner')
# print(res2)

# 并集合并, 重建索引
res2 = pd.concat([df5, df6], join='outer', ignore_index=True)
# print(res2)

# 列向合并 axis=1
res3 = pd.concat([df5, df6], axis=1)
# print(res3)

# 以df1的索引为准,
res3 = pd.concat([df5, df6], axis=1, join_axes=[df1.index])
print(res3)


#append



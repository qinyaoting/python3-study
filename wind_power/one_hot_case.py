import pandas as pd
import numpy as np

# 由list构造dataframe
df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']
])
print(df.head())
# 指定columns
df.columns = ['color', 'size', 'prize', 'label_tag']
size_mapping = {
    'XL': 3,
    'L': 2,
    'M': 1
}
# 将df中的字符串替换为字典的key
df['size'] = df['size'].map(size_mapping)
print(df.head())

tag_mapping = {lambda: idx for idx,label in enumerate(set(df['label_tag']))}
# df['label_tag'] = df['label_tag'].map(tag_mapping)
# print(df.head())

# 使用get_dummies进行one-hot编码
print(pd.get_dummies(df))

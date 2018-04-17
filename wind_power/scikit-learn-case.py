import numpy
import pandas as pd
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn_pandas import DataFrameMapper

# 由 [字典] 构造df
test_data = pd.DataFrame({'pet': ['cat', 'cat', 'dog', 'mouse'],
                          'age': [4, 6, 3, 3],
                          'salary': [4, 5, 1, 1]})
# 把df中age列编码为one hot
a1 = OneHotEncoder(sparse=False).fit_transform(test_data[['age']])
a2 = OneHotEncoder(sparse=False).fit_transform(test_data[['salary']])
# 合并a1 a2
final_out = numpy.hstack((a1, a2))
# print(final_out)

# 为两列同时编码
final_out2 = OneHotEncoder(sparse=False).fit_transform(test_data[['age', 'salary']])
# print(final_out2)


# DataFrameMapper将age列先最大最小值归一化，再标准化
mapper = DataFrameMapper([
    (['age'], [MinMaxScaler(), StandardScaler()])

])
result = mapper.fit_transform(test_data)
# print(result)

# 这三列做了二值化编码、最大最小值归一化等
mapper2 = DataFrameMapper([
    (['pet'], LabelBinarizer()),
    (['age'], MinMaxScaler()),
    (['salary'], OneHotEncoder())
])

result2 = mapper2.fit_transform(test_data)
# print(result2)

mapper3 = DataFrameMapper([
    (['salary', 'age'], [MinMaxScaler(), StandardScaler()])
])
# print(mapper3.fit_transform(test_data))


# 多列整体变换
# 对age和salary列分别进行了 PCA 和生成二次项特征
mapper4 = DataFrameMapper([
    (['salary', 'age'], [MinMaxScaler(), PCA(2)]),
    (['salary', 'age'], [MinMaxScaler(), PolynomialFeatures(2)])
])
# print(mapper4.fit_transform(test_data))


# 分类变量要变成二值化
mapper = DataFrameMapper([
    ('Continent', sklearn.preprocessing.LabelBinarizer()),
])
df = pd.DataFrame({'Continent': ['AM', 'EP', 'LA', 'AM']})
tempX = df[['Continent']].head()
# print(tempX)
# print(mapper.fit_transform(tempX.copy()))


# 由 [列表] 构造df, 指定列名称
test_mat = pd.DataFrame([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 0, 0]
], columns=['A', 'B', 'C', 'D'])
print(test_mat)
print(test_mat.index)
print(test_mat.columns)
print(test_mat.shape)
print(test_mat.describe())

# 将对应的列,进行编码
mapper9 = DataFrameMapper([
    (['A'], LabelBinarizer()),
    (['B', 'D'], MinMaxScaler()),
    (['C'], OneHotEncoder())
])
# print(mapper9.fit_transform(test_mat))

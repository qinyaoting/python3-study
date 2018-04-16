import numpy
import pandas as pd
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn_pandas import DataFrameMapper

test_data = pd.DataFrame({'pet': ['cat', 'cat', 'dog', 'mouse'],
                          'age': [4, 6, 3, 3],
                          'salary': [4, 5, 1, 1]})
a1 = OneHotEncoder(sparse=False).fit_transform(test_data[['age']])
a2 = OneHotEncoder(sparse=False).fit_transform(test_data[['salary']])
final_out = numpy.hstack((a1, a2))
# print(final_out)

final_out2 = OneHotEncoder(sparse=False).fit_transform(test_data[['age', 'salary']])

# print(final_out2)

# age列先最大最小值归一化，再标准化
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
    (['salary','age'], [MinMaxScaler(), PCA(2)]),
    (['salary', 'age'], [MinMaxScaler(), PolynomialFeatures(2)])
])

# print(mapper4.fit_transform(test_data))

# 分类变量要变成二值化
mapper = DataFrameMapper([
    ('Continent', sklearn.preprocessing.LabelBinarizer()),
])
df = pd.DataFrame({'Continent': ['AM', 'EP', 'LA', 'AM']})
tempX = df[['Continent']].head()
print(tempX)
print(mapper.fit_transform(tempX.copy()))

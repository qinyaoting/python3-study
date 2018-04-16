import numpy
import pandas as pd
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn_pandas import DataFrameMapper

test_data = pd.DataFrame({'pet': ['cat', 'cat', 'dog', 'mouse'],
                          'age': [4, 6, 3, 3],
                          'salary': [4, 5, 1, 1]})
encoded_data = OneHotEncoder(sparse=False).fit_transform(test_data[['age']])
print(test_data)
print(encoded_data)
a2 = OneHotEncoder(sparse=False).fit_transform(test_data[['salary']])
final_out = numpy.hstack((encoded_data, a2))
print(final_out)


final_out2 =OneHotEncoder(sparse = False).fit_transform(test_data[['age', 'salary']])

print(final_out2)



mapper = DataFrameMapper([
('Continent', sklearn.preprocessing.LabelBinarizer()),
])
df = pd.DataFrame({'Continent':['AM', 'EP', 'LA', 'AM']})
tempX = df[['Continent']].head()
print (tempX)
print (mapper.fit_transform(tempX.copy()))

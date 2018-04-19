import pandas as pd

df = pd.read_csv('WindPower2012.csv', error_bad_lines=False)

data2 = []
for i in range(len(df) // 12):
    data2.append(df[i * 12:(i + 1) * 12].mean())
data2 = pd.DataFrame(data2)
print("Length of hourly averaged data : ", len(data2))


print(data2.iloc[:, 5:13].describe())
# print(data2.info())




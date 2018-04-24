import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import matplotlib.pyplot as plt
from numpy import shape
import matplotlib.ticker as ticker
# %matplotlib inline



df = pd.read_excel("datatest.xlsx")
print("Length of original data : ", len(df))

# print(df.head())
print(df.info())


# 图1--x年月日,y游客人数

def line1():
    data_year = df[df.year == 2017]
    x1 = data_year['date']
    x1 = pd.date_range('20170101', periods=len(data_year))
    y1 = data_year['tourist_num']
    data = df.loc[:, ['date', 'tourist_num', 'year']]
    all_years = data.drop_duplicates(['year'])['year'].reset_index(drop=True)
    # 根据时间, 把多行合并为一个list
    # x周是1月1日到12月31日
    # y轴是4年的list
    dates = []
    points = []
    cur_type = 0
    cur_year = all_years[cur_type]
    print(all_years.index)
    print(len(all_years))
    print(all_years[1])
    months = np.arange(365)     #?1

    for i in range(len(data)):
        item = data.loc[i]
        if item['year'] == cur_year:
            dates.append(item['date'])
            points.append(item['tourist_num'])
        else:
            plt.legend(loc='best')

            plt.plot(months, points[0: 365], label=cur_year)        #?2     #?md
            cur_type += 1
            # if cur_type > 1:
            #     break
            cur_year = all_years[cur_type]
            dates = []
            points = []
            dates.append(item['date'])
            points.append(item['tourist_num'])


    # plt.xticks(x1)
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


# 图2--每个月的总数
def line2():
    df = pd.read_excel("datatest.xlsx")
    data = df.groupby(by=['year'])['tourist_num'].sum().to_frame()
    tourist_num_data = data['tourist_num']
    # 构建数据
    # print(data.head())
    # print(data.index)
    # 中文乱码处理
    # print(data[['tourist_num']])
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图
    plt.bar(range(111), tourist_num_data, align='center', color='steelblue', alpha=0.8)
    # 添加y轴标签
    plt.ylabel('GDP')
    # 添加标题
    plt.title('四个直辖市GDP打比平')
    # 添加刻度标签
    plt.xticks(range(12), ['北京市', '上海市', '天津市', '重庆市'])
    # 添加ｙ轴刻度范围
    plt.ylim([5000, 15000])
    # 为每隔条形图添加数字化标签
    for x, y in enumerate(data):
        print(x, '===', y)
        plt.text(x, y + 100, '%s' % round(y, 1), ha='center')

    plt.show()


# 图3-每年的总数

# 图4-三年的线合并起来

# 图5-上岛人数分布

if __name__ == '__main__':
    line1()
import numpy as np
import matplotlib.pyplot as plt

'''
直辖市GDP水平
https://www.kesci.com/apps/home/project/59ed8d7418ec724555a9b4c0

中国的四个直辖市分别为北京市、上海市、天津市和重庆市，其2017年上半年的GDP分别为
12406.8亿、13908.57亿、9386.87亿、9143.64亿。对于这样一组数据，我们该如何使用
条形图来展示各自的GDP水平呢？
'''

def level1_city_gdp():
    # 构建数据
    GDP = [12406.8, 13908.57, 9386.87, 9143.64]
    # 中文乱码处理
    plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图
    plt.bar(range(4), GDP, align='center',color='steelblue', alpha = 0.8)
    # 添加y轴标签
    plt.ylabel('GDP')
    # 添加标题
    plt.title('四个直辖市GDP打比平')
    # 添加刻度标签
    plt.xticks(range(4), ['北京市', '上海市', '天津市', '重庆市'])
    # 添加ｙ轴刻度范围
    plt.ylim([5000, 15000])
    # 为每隔条形图添加数字化标签
    for x, y in enumerate(GDP):
        print(x, '===', y)
        plt.text(x, y+100, '%s' % round(y, 1), ha='center')

    plt.show()


'''
同一本书不同平台最低价比较
很多人在买一本书的时候，都比较喜欢货比三家，例如《python数据分析实战》在亚马逊、当当网、
中国图书网、京东和天猫的最低价格分别为39.5、39.9、45.4、38.9、33.34
'''


def diff_book_price():
    # 构建数据
    price = [39.5, 39.9, 45.4, 38.9, 33.34]
    # 中文乱码的处理
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 绘图
    plt.barh(range(5), price, align='center', color = 'steelblue', alpha = 0.8)
    # 添加轴标签
    plt.xlabel('Price')
    # 添加标题
    plt.title('不同平台书的最低价比较')
    # 添加刻度标签
    plt.yticks(range(5), ['亚马逊', '当当网', '中国图书网', '京东', '天猫'])
    # 设置y轴刻度范围
    plt.xlim([32, 47])

    # 为每隔条形图添加数值标签
    for x, y in enumerate(price):
        plt.text(y + 0.1, x, '%s' % y, va='center')

    plt.show()

def family_capital_found_top5():
    Y2016 = [15600, 12700, 11300, 4270, 3620]
    Y2017 = [17400, 14800, 12000, 5200, 4020]
    labels = ['北京', '上海', '香港', '深圳', '广州']
    bar_width = 0.35
    # 中文乱码的处理
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.bar(np.arange(5), Y2016, label= '2016', color= 'steelblue', alpha=0.8, width=bar_width)
    plt.bar(np.arange(5) + bar_width, Y2017, label='2017', color='indianred', alpha = 0.8, width = bar_width)

    plt.xlabel('top5城市')
    plt.ylabel('家庭数量')

    plt.title('亿万财富家庭数Top5城市分布')

    plt.xticks(np.arange(5)+bar_width, labels)
    plt.ylim([2500, 19000])

    for x2016, y2016 in enumerate(Y2016):
        plt.text(x2016, y2016+100, '%s' % y2016)

    for x2017, y2017 in enumerate(Y2017):
        plt.text(x2017, y2017+100, '%s' % y2017)

    plt.legend()
    plt.show()


def line():
    y1 = [10, 13, 5, 40, 30, 60, 70, 12, 55, 25]
    x1 = range(0, 10)
    x2 = range(0, 10)
    y2 = [5, 8, 0, 30, 20, 40, 50, 10, 40, 15]
    plt.plot(x1, y1, label='Frist line', linewidth=3, color='r', marker='o',
             markerfacecolor='blue', markersize=12)
    # plt.plot(x2, y2, label='second line')
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # level1_city_gdp()
    # diff_book_price()
    family_capital_found_top5()

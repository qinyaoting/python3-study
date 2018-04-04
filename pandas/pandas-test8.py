import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 可视化控件

# Series 折线图
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 累加
data = data.cumsum()
# data.plot()
# plt.show()

# DataFrame 显示4组折线图
data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list('ABCD'))
data = data.cumsum()
# data.plot()
# plt.show()


# 1000行, 4列
# mat = np.random.randn(1000, 4)
# print(mat.size)
# print(mat)


# 显示一个分类的散点图
ax = data.plot.scatter(x= 'A', y= 'B',
                  color='DarkBlue', label = 'Class 1')
# plt.show()

# 显示两个类别的散点图
data.plot.scatter(x= 'A', y= 'C',
                  color='DarkGreen', label = 'Class 2', ax = ax)
# plt.show()

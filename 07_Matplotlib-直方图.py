import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'



""" ### Matplotlib-直方图 """
# x = np.random.randint(0, 10, 100)
# x
# # 统计每个元素出现的次数
# pd.Series(x).value_counts()

# # 直方图
# # bins: 组数
# plt.hist(x, bins=5)
# plt.hist(x, bins=[0, 3, 6, 9, 10])
# plt.savefig('images/5-9.png')



""" ### Pandas获取Excel数据 """
# df = pd.read_excel('data/plot.xlsx', sheet_name='hist')
# df
# x = df['分数']
# x.min(),  x.max()
# # 直方图
# # edgecolor: 边缘颜色
# plt.hist(x, bins=range(40, 110, 6), 
#          facecolor='b', edgecolor='k', alpha=0.4)
# plt.savefig('images/5-10.png')
# # plt.show()


""" # 概率分布 """
df = pd.read_excel('data/plot.xlsx', sheet_name='hist')
df
x = df['分数']
plt.hist(x, bins=range(40, 110, 6), facecolor='b', alpha=0.4, 
         edgecolor='k', density=True)
plt.show()
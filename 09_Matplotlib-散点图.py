""" ### Matplotlib-散点图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'


""" ### 散点图 """

# x = range(1, 7, 1)
# y = range(10, 70, 10)

# # 散点图
# plt.scatter(x, y, marker='o')
# plt.savefig('images/5-14.png')



""" ### 气泡图 """
# data = np.random.randn(100, 2)
# s = np.random.randint(50, 200, size=100)
# color = np.random.randn(100)

# plt.scatter(
#             data[:, 0],  # x坐标
#             data[:, 1],  # y坐标
#             s=s,  # 尺寸
#             c=color,  # 颜色
#             alpha=0.6  # 透明度
# ) 
# plt.savefig('images/5-15.png')





""" ### Pandas获取Excel数据 """
# df = pd.read_excel('data/plot.xlsx', sheet_name='scatter')
# df.head()
# x, y = df['广告费用'], df['销售收入']
# plt.figure(dpi=100)
# plt.scatter(x, y)

# plt.title('广告费用和销售收入之间的关系')
# plt.xlabel('广告费用')
# plt.ylabel('销售收入')
# plt.savefig('images/5-16.png')




""" ### 六边形图 """
df = pd.read_excel('data/plot.xlsx', sheet_name='scatter')
df.head()
x, y = df['广告费用'], df['销售收入']
plt.figure(dpi=100)

# 六边形图
# gridsize: 网格大小
# cmap: color map 颜色映射
#      rainbow: 彩虹色
plt.hexbin(x, y, gridsize=20, cmap="rainbow")

plt.title('广告费用和销售收入之间的关系')
plt.xlabel('广告费用')
plt.ylabel('销售收入')
plt.savefig('images/5-17.png')
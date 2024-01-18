""" ### Matplotlib-面积图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'



""" ### 面积图 """
# x = [1, 2, 3, 4, 5]
# y = np.random.randint(10, 100, 5)

# # 面积图
# plt.stackplot(x, y)
# plt.savefig('images/5-22.png')





""" ### Pandas获取Excel数据 """
# df = pd.read_excel('data/plot.xlsx', sheet_name='stackplot1')
# df
# x, y = df['年份'], df['销售额']
# plt.figure(dpi=100)

# plt.stackplot(x, y)
# plt.plot(x, y)
# plt.savefig('images/5-23.png')
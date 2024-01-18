import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'




""" ### 绘制一条线"""

# plt.figure(figsize=(8, 5))

# x = ["Mon", "Tues", "Wed", "Thur", "Fri","Sat","Sun"]
# y = [20, 40, 35, 55, 42, 80, 50]

# plt.plot(x, y, c="g", marker='D', markersize=5)

# #绘制坐标轴标签
# plt.xlabel("星期")
# plt.ylabel("活跃度")
# plt.title("Python语言活跃度")

# for x1, y1 in zip(x, y):
#     plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=16)

# plt.savefig('images/5-1.png')
# plt.show()



""" ### 绘制多条线 """

# plt.figure(figsize=(8, 5))

# x = np.random.randint(0, 10, size=15)

# plt.plot(x, marker='*', color='r')
# plt.plot(x.cumsum(), marker='o')

# plt.savefig('images/5-2.png')




""" ### Pandas获取Excel数据 """
df = pd.read_excel('data/plot.xlsx', sheet_name='line')
df.head()

x, y1, y2, y3 = df['月份'], df['语文'], df['数学'], df['英语']

# 画折线图
# 画布大小
plt.figure(figsize=(7, 4))

# ms: marker size 标记点的大小
# alpha: 透明度 0~1之间，1表式不透明，0表式完全透明
plt.plot(x, y1, label='语文', c='g', ls='--', marker='*', mfc='y', ms=10, alpha=0.5)
plt.plot(x, y2, label='数学', c='b', ls='-.', marker='o', mfc='w', ms=10)
plt.plot(x, y3, label='英语', c='r', ls=':', marker='+', mfc='w', ms=10, alpha=0.5)

plt.yticks(range(0, 110, 10))  # y轴的刻度
plt.ylabel('成绩')
plt.xlabel('月份')
plt.title('成绩的变化趋势')

plt.legend()  # 图例
plt.grid(axis='y')

plt.savefig('images/5-3.png')

plt.show()
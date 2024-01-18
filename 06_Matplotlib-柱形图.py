import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'


""" ### 简单柱状图 """
# fig = plt.figure(figsize=(8, 5))

# x = ['语文', '数学',  '英语', 'Python', '化学']
# y = [20, 10, 40, 60, 10]

# plt.bar(x, y)
# plt.show()






""" ### Pandas获取Excel数据 """
# df = pd.read_excel('data/plot.xlsx', sheet_name='bar1')
# df
# x, y = df.年份, df.销售额

# plt.figure(dpi=100)

# plt.title('2014年-2020年销售额')
# plt.xlabel('年份')
# plt.ylabel('销售额')

# # 柱形图
# plt.bar(x, y, width=0.6)

# # 给每个柱形图加上数字
# for a, b in zip(x, y):
#     plt.text(x=a, y=b+5e4, s='{:.1f}万'.format(b/10000), 
#                 ha='center', fontsize=9
#             )

# plt.savefig('images/5-5.png')

# plt.show()






""" ### 一次绘制多个柱状图 """
""" # 簇状柱形图 """

df2 = pd.read_excel('data/plot.xlsx', sheet_name='bar2')
df2
x, y1, y2, y3 = df2.年份,  df2.北区, df2.中区, df2.南区
plt.figure(dpi=100)
plt.title('2014年-2020年销售额')
plt.xlabel('年份')
plt.ylabel('销售额')

width=0.2
plt.bar(x-width, y1, width=width, label='北区')
plt.bar(x, y2, width=width, label='中区')
plt.bar(x+width, y3, width=width, label='南区')

plt.legend()
plt.savefig('images/5-6.png')

plt.show()







""" # 堆叠柱形图 """
plt.figure(dpi=100)
plt.title('2014年-2020年销售额')
plt.xlabel('年份')
plt.ylabel('销售额')

plt.bar(x, y1, label='北区')
plt.bar(x, y2, label='中区', bottom=y1)  # 画图的时候y轴的底部起始值
plt.bar(x, y3, label='南区', bottom=y1+y2)

plt.legend()
plt.savefig('images/5-7.png')

plt.show()




""" # 条形图 """

plt.barh(x, y1)
plt.savefig('images/5-8.png')

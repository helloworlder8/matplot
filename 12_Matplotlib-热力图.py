""" ### Matplotlib-热力图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'


""" ### 热力图 """
# df = pd.read_excel('data/plot.xlsx', sheet_name='imshow')
# df
# data = df.drop(columns='省份').values #丢弃
# y = df['省份']
# # x = df.columns[1:]
# x = df.drop(columns='省份').columns #列表
# data

# plt.figure(figsize=(14, 10))

# # 热力图
# plt.imshow(data, cmap='Blues')

# # 设置坐标轴刻度
# plt.xticks(range(len(x)), x)
# plt.yticks(range(len(y)), y)

# # 添加文字
# for i in range(len(x)):
#     for j in range(len(y)): 
#         plt.text(x=i, y=j, s=data[j, i], 
#                  ha='center', 
#                  va='center',
#                 fontsize=12
#                 )
    
# # 颜色条
# # plt.colorbar()
    
# plt.show()
""" ### Matplotlib-饼图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'


""" 简单示例 """
# x = [10, 20, 30, 40]

# plt.pie(x, autopct='%.1f%%')
# plt.savefig('images/5-18.png')
# plt.show()


""" ### Pandas获取Excel数据 """
# df = pd.read_excel('data/plot.xlsx', 
#                    sheet_name='pie1')
# df
# citys, values = df.省份, df.销量
# # 饼图
# plt.figure(figsize=(5, 5))
# plt.pie(
#             x=values,   # 值
#             autopct='%.1f%%',  # 百分比
#             labels=citys,  # 标签
#             pctdistance=0.8,  # 百分比文字的位置
#             explode=[0, 0, 0, 0.1, 0, 0.1, 0, 0, 0, 0],  # 分裂效果
#             # 字体样式
#             textprops={'fontsize': 12, 'color': 'blue'},
#             shadow=True
#        )

# plt.savefig('images/5-19.png')
# plt.show()



""" ### 单个圆环：甜甜圈 """
# df = pd.read_excel('data/plot.xlsx', 
#                    sheet_name='pie1')
# df
# citys, values = df.省份, df.销量
# # 饼图
# plt.pie(
#             x=values,   # 值
#             autopct='%.1f%%',  # 百分比
#             labels=citys,  # 标签
#             pctdistance=0.8,  # 百分比文字的位置
#             # 字体样式
#             textprops={'fontsize': 10, 'color': 'k'},
            
#             # 
#             wedgeprops={'width': 0.5, 'edgecolor': 'b'}
#        )

# plt.savefig('images/5-20.png')
# plt.show()





""" ### 多个圆环 """
# df1 = pd.read_excel('data/plot.xlsx', sheet_name='pie1')
# df2 = pd.read_excel('data/plot.xlsx', sheet_name='pie2')

# citys1, values1 = df1.省份, df1.销量
# citys2, values2 = df2.省份, df2.销量

# plt.figure(dpi=200)

# # 饼图
# plt.pie(
#             x=values1,   # 值
#             autopct='%.1f%%',  # 百分比
#             labels=citys1,  # 标签
#             pctdistance=0.8,  # 百分比文字的位置
#             # 字体样式
#             textprops={'fontsize': 10, 'color': 'k'},
            
#             # 
#             wedgeprops={'width': 0.4, 'edgecolor': 'w'}
#        )

# # 饼图
# plt.pie(
#             x=values2,   # 值
#             autopct='%.1f%%',  # 百分比
#            #  labels=citys2,  # 标签
#             pctdistance=0.8,  # 百分比文字的位置
#             # 字体样式
#             textprops={'fontsize': 8, 'color': 'k'},
#             # 半径 
#             radius=0.6
#        ) 

# plt.legend(citys1, fontsize=3)
# plt.savefig('images/5-21.png')
# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'



""" #### 图例
- legend """

# fig = plt.figure(figsize=(8, 5))

# x = np.linspace(0, 2*np.pi)
# plt.plot(x, np.sin(x), label='sin')
# plt.plot(x, np.cos(x), label='cos')

# # 图例
# plt.legend()



""" #### 图例
- legend """
# fig = plt.figure(figsize=(8, 5))

# x = np.linspace(0, 2*np.pi)
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

# # 图例
# plt.legend(['Sin', 'Cos'], 
#            fontsize=18, 
#            loc='center',  # 居中
#            ncol=2,   # 显示成几列
           
#            # bbox_to_anchor = [x, y, width, height]
#            bbox_to_anchor=[0, 0.8, 1, 0.2]  # 图例的具体位置
#           )




""" ####  线条属性
- color 颜色
- linestyle 样式
- linewidth 宽度
- alpha 透明度
- marker 标记
- mfc: marker face color 标记的背景颜色 """

# fig = plt.figure(figsize=(8, 5))
# x = np.linspace(0, 2*np.pi, 20)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # c : color 线颜色
# # marker: 标记的样式或点的样式
# # mfc: marker face color 标记的背景颜色
# # ls : line style 线的样式
# # lw: line width 线的宽度
# # label: 线标签（图例中显示）
# plt.plot(x, y1, c='r', marker='o', ls='--', lw=1, label='sinx', mfc='y', )

# plt.plot(x, y2, c='b', marker='*', ls='-', lw=2, label='cosx', mfc='g', )

# plt.plot(x, y1-y2, c='y', marker='^', ls='-', lw=3, label='sinx-cosx', mfc='b', alpha=0.5)

# plt.plot(x, y1+y2, c='orange', marker='>', ls='-.', lw=4, label='sinx+cosx', 
#          mfc='y', 
#          markersize=10,  # 点大小
#          markeredgecolor='green',  #点边缘颜色
#          markeredgewidth=2  # 点边缘宽度
#         )

# # 图例
# plt.legend()

# plt.savefig('images/4-2.png')




""" #### 坐标轴刻度
- xticks
- yticks """


# # 图形绘制
# x = np.linspace(0, 10) 
# y = np.sin(x)   
# plt.plot(x,y)

# # 设置x轴y轴刻度
# plt.xticks(np.arange(0, 11, 1))
# plt.yticks([-1, 0, 1])

# plt.savefig('images/4-3.png')
# plt.show()




""" #### 坐标轴刻度
- xticks
- yticks """
# # 图形绘制
# x = np.linspace(0, 10) 
# y = np.sin(x)   
# plt.plot(x,y)

# # 设置x轴y轴刻度标签
# plt.yticks(ticks=[-1, 0, 1],    # 刻度值
#                labels=['min', '0', 'max'],  # 刻度值对应的标签名（显示）
#                fontsize=20,   # 文字大小
#                ha='right',  # 水平对齐方式
#                color='blue'  # 颜色
#           )
# plt.xticks(ticks=np.arange(0, 11, 1), fontsize=20, color='red' )
# plt.savefig('images/4-4.png')
# plt.show()





""" #### 坐标轴范围
- xlim
- ylim """

# # sin曲线
# x = np.linspace(0, 2*np.pi)
# y = np.sin(x)
# plt.plot(x, y, c='r')

# # 设置x轴范围
# plt.xlim(-2, 8)

# # # 设置 y轴范围
# plt.ylim(-2, 2)
# plt.savefig('images/4-5.png')





""" #### 坐标轴配置
- axis """
# # sin曲线
# x = np.linspace(0, 2*np.pi)
# y = np.sin(x)
# plt.plot(x, y, c='r')

# # 坐标轴范围：[xmin, xmax, ymin, ymax]
# plt.axis([-2, 8, -2, 2])

# # 选项
# # off ： 不显示坐标轴
# # equal: 让x轴和y轴 刻度距离相等
# # scaled：自动缩放坐标轴和图片适配
# # tight：紧凑型自动适配图片
# # square：x轴和y轴宽高相同
# plt.axis('square')
# plt.savefig('images/4-6.png')

# plt.show()





""" ####  标题 和 网格
- title 
- grid """

# 图形绘制
# x = np.linspace(0, 10) 
# y = np.sin(x)   
# plt.plot(x, y)

# # 图的标题
# # fontsize : 标题大小
# # loc：标题位置
# plt.title('sin曲线', fontsize=20, loc='center')
# # 父标题
# plt.suptitle('父标题', 
#              y=1.1,  # 位置
#              fontsize=30 #文字大小
#             )  

# # 网格线
# # ls: line style 网格线样式
# # lw：line width  网格线宽度
# # c: color 网格线颜色
# # axis：画哪个轴的网格线，默认x轴和y轴都画
# plt.grid(ls='--', lw=0.5, c='gray', axis='y')
# plt.savefig('images/4-7.png')

# plt.show()





""" #### 标签
- xlabel
- ylabel """


# # 图形绘制
# x = np.linspace(0, 10) 
# y = np.sin(x)   
# plt.plot(x, y)

# # 坐标轴标签
# plt.xlabel('y=sin(x)', 
#                fontsize=20,   # 文字大小
#                rotation=0,  # 旋转角度
#           )
# plt.ylabel('y=sin(x)', 
#             rotation=90,  # 旋转角度
#             horizontalalignment='right',   # 水平对齐方式
#             fontsize=20 
#           )

# # 标题
# plt.title('正弦曲线')
# plt.savefig('images/4-8.png')




""" #### 文本
- text """

# plt.figure(figsize=(8, 5))

# x = np.linspace(0, 10, 10)
# y = np.array([60, 30, 20, 90, 40, 60, 50, 80, 70, 30])
# plt.plot(x, y, ls='--', marker='o')

# # 文字
# for a, b in zip(x, y):
#     # 画文本
#     plt.text(
#             x=a+0.3,  # x坐标
#             y=b+0.5,  # y坐标
#             s=b,  # 文字内容
#             ha='center',  # 水平居中
#             va='center',   # 垂直居中
#             fontsize=14,  # 文字大小
#             color='r'  # 文字颜色
#     )
    
# plt.savefig('images/4-9.png')
# plt.show()




""" #### 注释
- annotate """

# plt.figure(figsize=(8, 5))

# x = np.linspace(0, 10, 10)
# y = np.array([60, 30, 20, 90, 40, 60, 50, 80, 70, 30])
# plt.plot(x, y, ls='--', marker='o')

# # 注释（标注）
# plt.annotate(
#     text='最高销量',  # 标注的内容
#     xy=(3, 90),  # 标注的坐标点
#     xytext=(1, 80),  # 标注的内容的坐标点
#     # 箭头样式
#     arrowprops={
#                 'width': 2,   # 箭头线的宽度 
#                 'headwidth': 8,  # 箭头头部的宽度
#                 'facecolor': 'blue'  # 箭头的背景颜色
#     }
# )
# plt.savefig('images/4-10.png')





""" #### 保存图片
- savefig """
# 图形绘制
f = plt.figure(figsize=(8, 5))

x = np.linspace(0, 2*np.pi) 
plt.plot(x, np.sin(x) )
plt.plot(x, np.cos(x)) 

f.savefig(
            fname='pic_name2.png',  # 文件名：png、jpg、pdf
            dpi=100,  # 保存图片像素密度
            facecolor='pink',  # 背景颜色
            edgecolor='lightgreen',  # 边界颜色
            bbox_inches='tight',  # 保存图片完整
            pad_inches=1  # 内边距
)  
# plt.savefig('images/4-11.png')
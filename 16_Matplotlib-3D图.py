""" ### Matplotlib-3D图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'
# 3D引擎
from mpl_toolkits.mplot3d.axes3d import Axes3D 




""" 简单实例 """
# fig = plt.figure(figsize=(8, 5))  

# x = np.linspace(0, 100, 400)
# y = np.sin(x)
# z = np.cos(x)

# # 三维折线图
# axes = Axes3D(fig, auto_add_to_figure=False) 
# fig.add_axes(axes)
# axes.plot(x,y,z) 
# plt.savefig('images/6-1.png')




""" 散点 """
# fig = plt.figure(figsize=(8, 5))  

# # 三维折线图
# axes = Axes3D(fig, auto_add_to_figure=False) 
# fig.add_axes(axes)

# # 三维散点图
# x = np.random.rand(50)  
# y = np.random.rand(50)  
# z = np.random.rand(50) 
# axes.scatter(x, y, z,
#                     color='red',
#                     s=100)
# plt.savefig('images/6-2.png')






fig = plt.figure(figsize=(8, 5))

# 二维变成了三维
axes = Axes3D(fig, auto_add_to_figure=False) 
fig.add_axes(axes)

x = np.arange(1, 5)

for m in x:
    axes.bar(
            np.arange(4),
            np.random.randint(10, 100, size=4),
            zs=m,  # 在x轴中的第几个
            zdir='x',  # 在哪个方向上排列
            alpha=0.7,  # 透明度
            width=0.5  # 宽度
    )
    
axes.set_xlabel('X轴', fontsize=18, color='red')
axes.set_ylabel('Y轴', fontsize=18, color='blue')
axes.set_zlabel('Z轴', fontsize=18, color='green')
plt.savefig('images/6-3.png')
plt.show()
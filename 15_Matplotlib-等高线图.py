""" ### Matplotlib-等高线图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

""" ### 等高线图
- 等高线图：也称水平图，是一种在二维平面上显示 3D 图像的方法 """

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# 将上述数据变成网格数据形式
X, Y = np.meshgrid(x, y)

# 定义Z与X, Y之间的关系
Z = np.sqrt(X**2 + Y**2)

# 画等高线
cp = plt.contourf(X, Y, Z)
# 颜色柱
plt.colorbar(cp) 
plt.savefig('images/5-27.png')
plt.show()
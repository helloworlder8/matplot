""" ### Matplotlib-极坐标图 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

""" ### 极坐标图 """
N = 8  # 分成8份

x = np.linspace(0,  2*np.pi, N, endpoint=False)   # 360度等分成8份
height = np.random.randint(3, 15, size=N)  # 值

width = np.pi / 4  # 宽度
colors = np.random.rand(8, 3)  # 随机颜色

# polar表示极坐标
ax = plt.subplot(111,  projection='polar') 
ax.bar(x=x, height=height, width=width, bottom=1, color=colors)
plt.savefig('images/5-25.png')
""" ### Matplotlib-雷达图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

""" ### 雷达图 """
fig = plt.figure(figsize=(6, 6))

x = np.linspace(0, 2*np.pi, 6, endpoint=False)
y = [83, 61, 95, 67, 76, 88]

# 保证首位相连
x = np.concatenate((x, [x[0]]))
y = np.concatenate((y, [y[0]]))

# 雷达图
axes = plt.subplot(111, polar=True)   

axes.plot(x, y, 'o-', linewidth=2)  # 连线
axes.fill(x, y, alpha=0.3)  # 填充

# 显示刻度
axes.set_rgrids([20, 40, 60, 80], fontsize=14)
plt.savefig('images/5-26.png')
plt.show()
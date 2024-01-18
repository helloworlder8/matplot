import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'   
plt.rcParams['axes.unicode_minus'] = False  





""" 字体 """
from matplotlib.font_manager import FontManager
fm = FontManager()
my_fonts = set(f.name for f in fm.ttflist)
my_fonts  





# """ 绘制抛物线 """
x = np.linspace(-5, 5, 50)
y =  x**2
plt.plot(x, y)
plt.grid() 
plt.show()
plt.savefig('images/1-1.png')





""" 画布配置 """
fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#11aa11')
# 绘制正弦曲线
x = np.linspace(0, 2*np.pi) 
y = np.sin(x)   
plt.plot(x,y)
fig.savefig('images/2-3.png')





# """ 在一个画布上绘制多个图 """
# x = np.linspace(0, 8) 
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x), 'r')
# plt.plot(x, -np.sin(x), 'g--')
# plt.savefig('images/2-4.png')



""" 立刻显示图片  """
# x = np.linspace(0, 8) 
# plt.plot(x, np.sin(x))
# plt.show() 
# plt.plot(x, np.cos(x), 'r')
# plt.plot(x, -np.sin(x), 'g--')
# plt.savefig('images/2-5.png')
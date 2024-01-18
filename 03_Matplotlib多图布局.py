import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'   
plt.rcParams['axes.unicode_minus'] = False  



""" subplot()函数 """
# # 2行2列
# fig = plt.figure(figsize=(8, 5))

# x = np.linspace(-np.pi, np.pi, 30)
# y = np.sin(x)

# # 子图1
# axes1 = plt.subplot(221)  # 2行2列的第1个子视图
# axes1.plot(x, y)
# axes1.set_title('子图1')

# # 子图2
# axes2 = plt.subplot(222)  # 2行2列的第2个子视图
# axes2.plot(x, y)
# axes2.set_title('子图2')

# # 子图3
# axes3 = plt.subplot(223)  # 2行2列的第3个子视图
# axes3.plot(x, y)
# axes3.set_title('子图3')

# # 子图4
# axes4 = plt.subplot(2, 2, 4)  # 2行2列的第4个子视图
# axes4.plot(x, y)
# axes4.set_title('子图4')

# # 自动调整布局
# fig.tight_layout()
# plt.savefig('images/3-1.png')





""" subplot()函数 """
# plt.figure(figsize=(8, 5))

# x = np.linspace(-np.pi, np.pi, 30)
# y = np.sin(x)

# # 子图1
# axes1 = plt.subplot(2, 2, 1)  
# axes1.plot(x, y, color='red')

# # 子图2
# axes2 = plt.subplot(2, 2, 2)
# lines = axes2.plot(x, y)
# lines[0].set_marker('*')   # 点的样式

# # 子图3
# axes3 = plt.subplot(2, 1, 2)  # 2行1列的第2行
# axes3.plot(x, np.sin(x*x))
# plt.savefig('images/3-2.png')





""" - 图形嵌套
- add_subplot()函数 """

# fig = plt.figure(figsize=(8, 5))

# # 使用 add_subplot() 函数
# # 图1
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.plot([1, 3])

# # 图2
# axes2 = fig.add_subplot(2, 2, 1, facecolor='pink')
# axes2.plot([1, 3])

# plt.savefig('images/3-3.png')




""" - 使用 axes() 函数
- 使用 add_axes() 函数 """

# fig = plt.figure(figsize=(8, 5)) 

# # 图1
# x = np.linspace(0, 2*np.pi, 30)
# y = np.sin(x)
# plt.plot(x, y)

# # 图2
# # [left, bottom, width, height]
# axes1 = plt.axes([0.55, 0.55, 0.3, 0.3])  
# axes1.plot(x, y, color='g')

# # 图3
# axes2 = fig.add_axes([0.2, 0.2, 0.25, 0.25]) 
# axes2.plot(x, y, color='r')

# plt.savefig('images/3-4.png')






""" - 使用 subplots() 函数 """

# x = np.linspace(0, 2*np.pi)

# # 3行3列
# # subplots：一次性返回9个子图
# fig, ax = plt.subplots(3, 3)
# ax1, ax2, ax3 = ax
# ax11, ax12, ax13 = ax1
# ax21, ax22, ax23 = ax2
# ax31, ax32, ax33 = ax3

# # fig来设置画布大小
# fig.set_figwidth(8)
# fig.set_figheight(5)

# ax11.plot(x, np.sin(x))
# ax12.plot(x, np.cos(x))
# ax13.plot(x, np.tanh(x))
# ax21.plot(x, np.tan(x))
# ax22.plot(x, np.cosh(x))
# ax23.plot(x, np.sinh(x))
# ax31.plot(x, np.sin(x) + np.cos(x))
# ax32.plot(x, np.sin(x*x) + np.cos(x*x))
# ax33.plot(x, np.sin(x)*np.cos(x))

# # 自动调整布局
# plt.tight_layout()

# plt.savefig('images/3-5.png')






""" - 双轴显示 """

# plt.figure(figsize=(8, 5))

# x = np.linspace(0, 10, 100)

# # 图1
# axes1 = plt.gca()  # 获取当前轴域
# axes1.plot(x, np.exp(x), color='red') 

# axes1.set_xlabel('time')  
# axes1.set_ylabel('exp', color='red')
# axes1.tick_params(axis='y', labelcolor='red') 

# # 图2
# axes2 = axes1.twinx()  # 和图1共享x轴
# axes2.set_ylabel('sin', color='blue')
# axes2.plot(x, np.sin(x), color='blue')
# axes2.tick_params(axis='y', labelcolor='blue')

# plt.tight_layout() 

# plt.savefig('images/3-6.png')
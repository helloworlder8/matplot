""" ### Matplotlib-箱型图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'


""" ### 箱型图 """
# x = [1, 2, 3, 5, 7, 9, -10]

# # 箱型图
# plt.boxplot(x)
# plt.savefig('images/5-11.png')
# plt.show()

# # 最大值
# # 3/4
# # 中位数
# # 1/4
# # 最小值

# # 异常值




""" ### 一次画多个箱型图 """

# x1 = np.random.randint(10, 100, 100)
# x2 = np.random.randint(10, 100, 100)
# x3 = np.random.randint(10, 100, 100)

# plt.boxplot([x1, x2, x3])
# plt.savefig('images/5-12.png')
# plt.show()




""" ### 一次画多个箱型图 """
data=np.random.normal(size=(500, 4)) 
lables = ['A','B','C','D']

# 画图
plt.boxplot(data, 
            notch=True,   # 箱型图样式
            sym='go',  # 颜色+marker样式
            labels=lables  # x轴标签
)  
plt.savefig('images/5-13.png')
plt.show()
""" ### Matplotlib-图像处理 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



img = plt.imread('data/pandas.jpeg')
img



""" ### 显示图片
- imshow """
# plt.imshow(img)
# plt.savefig('images/7-1.png')




""" # 垂直翻转显示 """
# plt.imshow(img, origin='lower')

# # 或
# plt.imshow(img[::-1])

# plt.savefig('images/7-2.png')


""" # 水平翻转 """
plt.imshow(img[:, ::-1])

plt.savefig('images/7-3.png')
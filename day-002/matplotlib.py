import matplotlib.pyplot as plt  # 为方便简介为plt
import numpy as np  # 画图过程中会使用numpy
import pandas as pd  # 画图过程中会使用pandas

x = np.arange(-5,5,0.1)  # 定义x数据范围
x=np.arange(-100,100,1)
y1 = x*3  # 定义y1数据范围
y2 = x*x  # 定义y2数据范围

#创建窗口、子图
fig = plt.figure()  # 先创建窗口一个窗口
ax1 = fig.add_subplot(3,1,1)  #通过fig添加子图，参数：行数，列数，第几个。
ax2 = fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
ax1.plot(x,y1)  # plot()画出曲线

ax2.plot(x,y2,color = 'red',marker = '*', linestyle = '--')  # 设置曲线颜色、线标记，线样式
plt.show() # 显示图像
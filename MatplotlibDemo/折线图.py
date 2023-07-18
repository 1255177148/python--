import numpy as np
import pandas as pd
import pylab

pylab.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
pylab.rcParams['axes.unicode_minus'] = False # 显示负号，坐标轴上的负号显示

x = np.arange(0, 1, 0.05) # X轴坐标点
y = [i * i for i in np.arange(0, 1, 0.05)] # Y轴坐标点
pylab.plot(x, y, "g-")

pylab.xlabel('横坐标') # X轴的描述
pylab.ylabel('纵坐标') # Y轴的描述
pylab.show()
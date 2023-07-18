import numpy as np

a = np.arange(180).reshape(3, 5, 6, 2) # arange生成一个numpy数组

print(a)
print(a.shape) # 数组的维度
print(a.ndim) # 维度的数量，就是shape的长度
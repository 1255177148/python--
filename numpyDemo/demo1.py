import numpy as np

'''
numpy可以用来:
1、数组的算数和逻辑运算;
2、傅里叶变换和用于图形操作的例程;
3、与线性代数有关的操作。numpy用于线性代数和随机数生成的内置函数
'''

a = np.arange(180).reshape(3, 5, 6, 2) # arange生成一个numpy数组

print(a)
print(a.shape) # 数组的维度
print(a.ndim) # 维度的数量，就是shape的长度
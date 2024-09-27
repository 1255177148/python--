a = '21'
print(int(a))

# eval()
print('10+10')
print(eval('10+10')) # 执行表达式里的运算并返回运算后的结果

# 实现list,dict,tuple和str之间的转换
str1 = '[[1, 2, 3], [4, 5]]'
print(type(str1))
li = eval(str1)
print(type(li))
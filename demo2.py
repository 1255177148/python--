'''
Author: elvis.he
Date: 2023-04-11 13:30:43
LastEditors: elvis.he
LastEditTime: 2023-06-07 13:52:21
FilePath: \python程序\demo2.py
Description: 

Copyright (c) 2023 by elvis.he, All Rights Reserved. 
'''
import os

oldList = [1, 2, 3]
newList = [i * 2 for i in oldList]
print(newList)
a = [i * 2 for i in oldList if i == 1]
print(a)

try:
    b = 3 / 1
except Exception as e:
    raise e

fun = lambda x,y: x + y
print(fun(2, 3))

str = "一个糖果"
print(str.find("果"))

relPath = os.path.realpath
print(relPath)

absPath = os.path.abspath
print(absPath)

'''
用with...as...的语法读取文件，这种语法的好处是，可以不用手动关闭输入输出流，会自动关闭
'''
with open("D://appshotInfo.txt", encoding = "UTF-8") as file:
    data = file.read()
print(data)
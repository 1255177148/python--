import json
from jsonpath import jsonpath

data = json.load(open('data3.json', 'r', encoding='utf-8'))
# 使用jsonpath提取数据
'''
简单的jsonpath使用
1、$  表示根节点
2、@  表示当前节点
3、.或者[]  表示子节点
4、[]  迭代器标识(可以在里面做简单的迭代操作，如数组下标，根据内容选值等)
等等...还有很多用法，具体可以在网上搜索下
'''
title = jsonpath(data, '$.title')
name = jsonpath(data, '$...name')
photo = jsonpath(data, '$.author.photo')
print(title, name, photo)
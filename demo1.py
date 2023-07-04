'''
Author: elvis.he
Date: 2023-02-27 16:00:13
LastEditors: elvis.he
LastEditTime: 2023-03-02 14:21:17
FilePath: \python程序\demo1.py
Description: 

Copyright (c) 2023 by elvis.he, All Rights Reserved. 
'''
print("hello world")
a = 1


def test(name: str) -> None:
    """
    Args:
        name (str): 名称
    """
    print(name)


def add(*number: int) -> int:
    return sum(number)


b = 2
if a == 2:
    print("111")
test("哈哈")
print(add(1, 2, 3))


def keyMap(**map):
    print(map)


maps = {'key1': 'value1', 'key2': 'value2'}
keyMap(**maps)

d = {'name': '小明', 'age': 15, 'sex': '男'}
s1, s2, s3 = d
print(s1)
print(s2)
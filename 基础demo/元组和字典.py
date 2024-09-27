# 元组，和列表的唯一区别是元组不允许修改，是只读的
arr = (1, 2, 3)
print(type(arr))


# 字典
map = {'name': 'test', 'age': 16}
print(type(map))
print(map)
# 字典常见操作
# 查看元素
print(map['name'])
print(map.get('age'))
print(map.get('phone'))
print(map.get('phone', '不存在'))
# 修改元素
map['phone'] = 123456
print(map)
map['phone'] = 123
print(map)
# 删除元素
# del 字典名   就会将指定的字典整个删除
# 字典名.clear() 清空整个字典，但会保留这个字典，可以继续新增元素
map.pop('name')
print(map)
# 返回字典里包含的所有键名
print(map.keys())
for i in map.keys():
    print(i)

# 返回字典里所有的值
print(map.values())
for i in map.values():
    print(i)

# 返回字典里所有的键值对
print(map.items())
for item in map.items():
    print(item)
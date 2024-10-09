li = ['one', 'two', 'three']
li.append('four')
print(li)
li.extend(['five', 'six']) # 向列表追加一个新列表，也就是将另一个列表的所有元素分别加到原有列表里
print(li)
li.append(None)
li.append(None) # 列表允许添加多个None
print(li)

for item in li:
    # comment: 
    print(item)
# end for

# 删除
del li[1]
print(li)
li.remove('f')
print(li)

# 排序
li.sort()
print(li)
li.reverse()
print(li)
li = ['one', 'two', 'three']
li.append('four')
print(li)
li.extend('five')
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
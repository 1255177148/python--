# 字符串编码
a = 'hello'
enco = a.encode() # 编码
print(type(enco))
deco = enco.decode() # 解码
print(type(deco))

# 字符串常见操作
str = 'abcabc'
print(str.find('a'))
print(str.find('a', -1))
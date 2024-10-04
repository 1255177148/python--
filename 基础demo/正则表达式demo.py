import re

# 匹配单个字符
# 1、匹配任意一个字符，除\n外-----常用
res = re.match('.', 'hello')
print(res.group())
# 2、[] 匹配 []中列举的字符,开头只要匹配到[]中的任意一个字符，都视为匹配成功-------常用
print(re.match('[hg]', 'hello').group())
print(re.match('[0-9]', '123').group()) # [0-9]表示匹配0到9之间的数字
print(re.match('[a-zA-Z]', 'Hello').group()) # [a-zA-Z]表示匹配所有大小写字母
# 3、匹配数字，使用\d
print(re.match('\d', '12345').group())
# 4、匹配非数字，使用\D
print(re.match('\D', '!adf').group())
# 5、匹配空白，即空格和tab键，使用\s
print(re.match('\s\s','     123').group())
# 6、匹配非空白，使用\S
print(re.match('\S', '&234').group())
# 7、\w，用来匹配单词字符，即大小写英文字母，数字，汉字和下划线--------常用
print(re.match('\w', '_123').group())
print(re.match('\w', '哈喽').group())
print(re.match('\w', '123').group())
# 8、\W，用来匹配非单词字符，即非大小写英文字母、数字、汉字和下划线
print(re.match('\W', '!@#').group())

# 匹配多个字符
# 1、*  匹配前一个字符出现0次或者无数次，即可有可无-----常用
print(re.match('\w*', 'abcd.').group())
# 2、+  匹配前一个字符出现1次或者无数次，即至少出现1次----常用
print(re.match('\w+', 'hello!').group())
# 3、？ 匹配前一次字符出现1次或者0次------常用
print(re.match('\d?', 'hello').group()) # 这里返回空，因为没有匹配到数字
# 4、{n}  匹配前一个字符出现n次
print(re.match('\w{2}', 'hello').group())
# 5、{n,m}   匹配前一个字符出现从n次到m次
print(re.match('\w{1,3}', 'hello').group())

# 匹配开头和结尾
# 1、^  :表示以...开头，或者表示对...取反 
print(re.match('^he', 'hello').group()) # 这里是匹配表示以...开头
print(re.match('[^he]', 'olleh').group()) # 这里是匹配非...开头的字符，现在示例的是表示非he开头的
# 2、$  :表示匹配以...结尾
print(re.match('\w{5}$', 'world').group())

# 匹配分组
# 1、|  表示匹配左右任意一个表达式-----常用
print(re.match('adc|def', 'def').group()) # 这里先匹配左边的abc，发现匹配不到，然后再匹配右边的def，然后就匹配到了
# 2、 (ab) 将括号里的字符作为一个分组----常用
print(re.match('\w*@(163|qq|foxmail).com', '1234@qq.com').group())
# 3、\num  匹配分组即()num匹配到的字符串,num为几就是匹配到第几个小括号里的内容 ----经常在匹配标签时使用
res = re.match(r'<(\w*)><(\w*)>login</\2></\1>','<html><body>login</body></html>') # 注意，这里的\1和\2匹配的是前面对应小括号里匹配的结果，而不是小括号里的表达式
print(res.group())

# 综合应用例子
# 匹配网址www开头，.com或者.cn结尾
li = ['www.baidu.com', 'www.hao123.com', 'www.py.cn', 'www.py.en']
# response = re.match('w{3}.\w*.(com|cn)', 'www.baidu.com')
# print(response.group())
for i in li:
    response = re.match(r'w{3}(.)\w*\1(com|cn)', i)
    if response:
        print(response.group())
    else:
        print(f'网址{i}没有匹配成功')


# 高级用法
# 1、search() 扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败，返回None
print(re.search('\d', 'pthon2').group())
# 2、findall() 从头到尾匹配，找到所有匹配成功的数据，返回一个匹配成功的数据列表
print(re.findall('\d', '123adv456'))
# 3、sub(pattern, repl, string, count) 根据正则表达式替换字符串
# pattern  正则表达式，表示要匹配被替换掉的字符
# repl     要替换的新内容
# string   需要匹配并被替换内容的字符串
# count    指定替换的次数，不传默认替换所有匹配到的内容
print(re.sub('\d', '2', '9月的第10天')) # 这里没有传count，替换掉了所有数字字符
print(re.sub('\d', '2', '9月的第10天', 1)) # 这里传了count，只替换1次
# 4、split(pattern, string, maxsplit) 根据正则表达式分割字符串
# pattern 传入要匹配分割的正则表达式，根据这个参数匹配字符，根据匹配到的字符分割字符串
# string  要被分割的字符
# maxsplit  最大分割次数
print(re.split(',', '123,456,789', 1))

# 贪婪与非贪婪匹配
# 1、贪婪匹配(默认)，在满足匹配规则时，匹配尽可能长的字符串
print(re.match('em*', 'emmmmmmmmm...').group())
# 2、非贪婪匹配，在匹配多个字符时，后面加上?，就表示时非贪婪匹配
print(re.match('em+?', 'emmmmmmmm..').group()) # 这里+表示匹配一次或者无数次，后面加上?后，是最少匹配，就表示只匹配一次
print(re.match('em{2,5}?', 'emmmmmmmmmmmmmmm..').group()) # 这里{2,5}表示匹配2到5次，后面加上?后，就表示只匹配2次
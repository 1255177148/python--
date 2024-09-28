# 必备参数（位置参数）
# 传递和定义参数的顺序及个数必须一致


# 默认参数
def demo1(a, b=12):
    """
    Purpose:
    """
    print(a)
    print(b)


# end def

demo1(1)


# 可变参数,参数以元组(tuple)形式接收
def demo2(*a):
    print(a)


demo2(1, 2)


# 可变关键字参数
def demo3(**kwargs):
    print(kwargs)


demo3(name="测试", age=18)

# 匿名函数
# 函数名 = lambda 形参 : 返回值(表达式)

# def add(a, b):
#     return a + b

add = lambda a, b: a + b
print(add(1, 5))

# lambda的参数形式
# 无参数
test1 = lambda : '返回一个结果'
print(test1())
# 一个参数
test2 = lambda name: name
print(test2('名字'))
# 默认参数
test3 = lambda name, age = 18 : (name, age)
print(test3('默认名字'))
# 可变参数
test4 = lambda **a : a
print(test4(name = '关键名字', age = 9))


# lambda匿名函数结合if判断
# 原来的if判断，简写
# a = 5
# b = 6
# print('a比b小') if a < b else print('a比b大')
comp = lambda a, b : 'a比b小' if a < b else 'a比b大'
print(comp(5, 6))
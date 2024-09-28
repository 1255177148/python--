# 闭包的三个条件
# 1、函数嵌套
# 2、内函数要使用外函数的局部变量
# 3、外函数的返回值是内函数的函数名

def outer():
    a = 1
    def inner(b):
         print(a + b)
    return inner

ot = outer()
ot(2)

# 装饰器

def outer1(fn):
    pre = '$'
    def inner1(a):
        print(pre + str(fn(a)))
    return inner1

# 装饰器第一种写法，使用@写在被装饰函数的上面，将sendNumber函数作为形参fn传入outer1函数
@outer1
def sendNumber(a) :
    return a

sendNumber(100)

# 装饰器第二种写法
def sendNum(a):
    return a

out = outer1(sendNum)
out(200)
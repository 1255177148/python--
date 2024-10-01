# 使用yield修饰，表示生成器，当使用next()方法时，依次执行到yield修饰的位置

def demo():
    print('生成器开始生效')
    yield 'a'
    yield 'b'
    yield 'c'

de = demo() # 将函数赋值给de，这时de就是一个生成器对象
print(type(de))
print(next(de))
print(next(de))
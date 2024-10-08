# 使用yield修饰，表示生成器，当使用next()方法时，依次执行到yield修饰的位置

# def demo():
#     print('生成器开始生效')
#     yield 'a'
#     yield 'b'
#     yield 'c'

# de = demo() # 将函数赋值给de，这时de就是一个生成器对象
# print(type(de))
# print(next(de))
# print(next(de))

# yield from 语法
# yield from 后面跟上一个可迭代对象，表示可以依次yield可迭代对象里的值

def sonGen():
    '''
    子生成器
    '''
    num = 0
    a = 0
    while True:
        newNum = yield a # 这里的newNum是下面proxyg.send()传进来的值，yield会将send传进来的值传给子生成器
        if newNum is None:
            break
        num = num + 1
        a  = newNum * num
    return num

def proxyGen():
    '''
    委托生成器
    '''
    while True:
        a = yield from sonGen()
        print('调用子生成器完毕，返回的值为：', a)

if __name__ == '__main__':
    proxyg = proxyGen()
    next(proxyg)
    print(proxyg.send(10))
    print(proxyg.send(15))
    print(proxyg.send(20))
    print(proxyg.send(None))
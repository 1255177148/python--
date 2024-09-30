# __new__() 方法，相当于Java中声明对象用的new，是为对象分配内存空间用的

class Person:
    
    def __new__(cls):
        print('我是__new__方法')
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print('我是__init__方法')

person = Person()

# 单例模式
# 第一种，通过重写__new__()实现单例模式
# 思路
# 定义一个类属性，初始值为None，用来记录单例对象的引用
# 重写__new__方法
# 进行判断，如果类属性是None，把__new__返回的对象引用保存进去
class Bachelor:
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

bachelor = Bachelor()

# 魔法属性
# 1、__doc__  类的描述信息
class Demo:
    '''类的注释文本'''
    pass

print(Demo.__doc__)
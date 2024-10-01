from collections.abc import Iterable #导入可迭代对象

# 使用 isinstance(o, type)可以判断指定的变量是否是可迭代对象，或者指定的type对象，type参数可以传入一个元组，
# 只要传入的变量符合type元组中的某一个对象，则返回true
a = 123
print(isinstance(a, Iterable))
print(isinstance(a, int))
print(isinstance(a, (int, Iterable)))

# 自定义一个迭代器，需要实现__iter__()和__next__()方法
class MyIterator:
    def __init__(self, current, end) -> None:
        self.current = current # 初始值
        self.end = end # 结束值
    
    def __iter__(self):
        '''返回对象本身'''
        return self
    
    def __next__(self):
        '''
        重写迭代器遍历方法，for循环获取时，都是调用此方法获取值
        '''
        if self.current > self.end:
            raise StopIteration
        cur = self.current
        self.current += 1
        return cur

myIterator = MyIterator(1, 20)
for i in myIterator:
    print(i)
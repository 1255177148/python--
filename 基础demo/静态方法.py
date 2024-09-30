# 使用@staticmethod来修饰

class Person:
    
    @staticmethod
    def study():
        print('我们会学习')

Person.study() # 可以直接用类访问静态方法
person = Person()
person.study() # 也可以用对象访问静态方法

# 类方法
# 使用装饰器@classmethod来修饰，对于类方法，第一个参数必须为类对象

class Human:
    
    @classmethod
    def sleep(cls):
        print('cls', cls)
        print('要睡觉')

Human.sleep()
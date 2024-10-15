class Person:
    name = '测试人'
    __age = 18 # 隐藏属性，前面用两个下划线声明这个是隐藏属性，子类不会集成隐藏属性，也不能被别的文件引用
    
    # 修改私有属性的方法
    def setAge(self, age):
        Person.__age = age
    
    # 私有方法
    def _play(self):
        print("玩游戏")

p = Person()
p._play()
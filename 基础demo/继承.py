class Person:
    def money(self):
        print('有一百万需要继承下去')

class Human:
    def eat(self):
        print('要吃饭')

class Man(Person, Human):
    def money(self):
        '''
        重写父类方法
        '''
        super().money()
        print('自己赚了一千万')

man = Man()
man.money()
man.eat()
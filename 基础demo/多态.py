class Animal:
    def roar(self):
        print('吼叫')


class Cat(Animal):
    def roar(self):
        print('喵喵叫')

class Dog(Animal):
    def roar(self):
        print('汪汪叫')

def test(obj):
    obj.roar()

cat = Cat()
dog = Dog()
test(cat)
test(dog)
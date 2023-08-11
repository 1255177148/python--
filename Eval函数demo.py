class EvalDemo:
    
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
        self.age = None
    
    def setAgeStr(self, age):
        self.age = age
    
    
    def evalStr(self):
        s = 'print("name=" + self.name + ";value=" + self.value + ";age=" + self.age)'
        eval(s)


if __name__ == '__main__':
    demo = EvalDemo('名字', '值')
    demo.setAgeStr('5')
    demo.evalStr()
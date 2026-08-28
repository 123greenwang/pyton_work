class Dog:
    '模拟小狗'
    def __init__(self,name,age):
        '初始属性'
        self.name=name
        self.age=age
        print(self)
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"
    def sit(self):
        print(f'{self.name} is now sitting')
    #def 
my_dog=Dog('wille',6)

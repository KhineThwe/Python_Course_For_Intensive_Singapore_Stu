"""
Muli-level
A

B

C
"""
class Animal:
    def __init__(self,name):
        self.name= name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)

    def give_birth(self):
        print(f'{self.name} is giving birth.')

class Dolphin(Mammal):
    def __init__(self,name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} is swimming')

if __name__ == '__main__':
    dolphin = Dolphin("Dory")
    dolphin.eat()
    dolphin.give_birth()
    dolphin.swim()
    dolphin.sleep()

    mammal = Mammal("Nemo")
    mammal.give_birth()
    mammal.eat()
    mammal.sleep()

    animal = Animal("NeNe")
    animal.eat()
    animal.sleep()
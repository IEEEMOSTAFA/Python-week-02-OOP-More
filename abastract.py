# from abc import ABC,abstractmethod
# #abstract base class

# class Animal(ABC):
#     @abstractmethod #enforce all derived class to have a eat method

#     def eat(self):
#         print('I eat food')
#     @abstractmethod
#     def move(self):
#         pass

# class Monkey(Animal):
#     def __init__(self,name) -> None:
#         self.catagory = 'Monkey'
#         self.name = name
#         super().__init__()    

#     def eat(self):
#         print('Hey na na na,I am eating banana')   

#     def move(self):
#         print('Hanging on the branches')     

# layka = Monkey('lucky')

# layka.eat()
# layka.move()

from abc import ABC,abstractmethod

class Animal(ABC):

    def eat(self):
        print('I eat food')

    @abstractmethod
    def move(self):
        pass 

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name = name
        self.catagory = 'Monkey'

        super().__init__()    

    def eat(self):
        print('Hey na  na  na ..I am eating banana')

    def move(self):
        print('Hanging on the branches')

odura = Monkey('lablo')                   
odura.eat()
odura.move()
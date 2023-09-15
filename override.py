class person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
     

     
    def eat(self):
        print('Vat mangso polau korma')    
    def exercise(self):
        raise NotImplementedError

class Cricketer(person):

    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team

        super().__init__(name, age, height, weight)
    # override
    def eat(self):
        print('vegetables') 

    def exercise(self):
        print('Gym  e poisa diya hudai gham jaorai')       

    # + sign operator  overload

    def __add__(self,other):
        return self.age + other.age
        # * sign operator  overload
    def __mul__(self,other):
        return self.weight * other.weight
        # operator  overload
    def __len__(self):
        return self.height
    
    def __gt__(self,other):
        
        return self.age > other.age
    

sakib = Cricketer('sakib',38,68,91,'sunrise')

mushi = Cricketer('mushi',36,65,78,'BD')

# sakib.eat()

# sakib.exercise()

#plus sign overload

print(45 + 63)

print('Sakib' + 'Rakib')

print([12,98] + [5,6,7,1,2])

print(sakib + mushi)

print(sakib * mushi)

print(len(sakib))

print(sakib > mushi)


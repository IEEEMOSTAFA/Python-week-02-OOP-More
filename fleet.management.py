# Ena Poribohon

class Company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []
        self.address = address
        

class Driver:
    def __init__(self,name,licence,age) -> None:
        self.licence = licence
        self.name = name
        self.age = age

    
        print( f'name: {self.name} age: {self.age} licence: {self.licence}')    


class Counter:
    def __init__(self) -> None:
        
     pass
    def purchase_a_ticket(self,start,destination):
        pass


class Passenger:
    pass

class Supervisor:
    pass

red_mia = Driver('a','123',32)


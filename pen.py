""" pen class create three object with different instance attribute """
class Pen:
    manufactured ="Bangladesh"
    def __init__(self,owner,brand,price,location):
        self.owner = owner
        self.brand = brand
        self.price = price
        self.location = location

my_pen = Pen('Mostafa','Matador',5.00,'Chittagong')
print(my_pen.owner,my_pen.brand,my_pen.price,my_pen.location)

her_pen = Pen('Nadia','Hi-School',6.0,'Comilla')
print(her_pen.owner,her_pen.brand,her_pen.price,her_pen.location)

sis_pen = Pen('Muna','Linux',10,'Dhaka')
print(sis_pen.owner,sis_pen.brand,sis_pen.price,sis_pen.location)
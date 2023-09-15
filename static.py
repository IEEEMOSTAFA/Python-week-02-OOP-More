#Static attribute (class attribute)
#Static method @staticmethod
#Class method @class method
#difference between static method and class method

class Shopping:
    cart = []  #class attribute otoba # static attribute
    origin = 'china'

    def __init__(self,name,location) -> None:
        self.name = name   # instance attribute
        self.location = location

    def purchase(self,item,price,amount):
           remaining =amount - price
           print(f'buying : {item} for price:{price} and remaning :{remaining}')

    @staticmethod
    def multiply(a,b):
        
        result =  a*b
        print(result)       
    @classmethod
    def hudai_deki(self,item):
      print('hudai dekhi kintu kinmu na just ac er hawa khaite aschi',item)



basundara = Shopping('basun dhara','not popular location')
# basundara.purchase('lungi',500,1000)
# Shopping.purchase(2,3,3)            
basundara.hudai_deki('lungi')

Shopping.hudai_deki('Lungi')
Shopping.multiply(4,6)# Static Method

basundara.multiply(6,9)
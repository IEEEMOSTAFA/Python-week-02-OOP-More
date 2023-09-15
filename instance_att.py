class Shop:
    sopping_mall ='Jabona'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # class is an instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


mehjabeen = Shop('Mez jab  eeen')
mehjabeen.add_to_cart('Shoe')            
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

niso = Shop('nisi night er nisho')
niso.add_to_cart('hat')
niso.add_to_cart('watch')
print(niso.cart)

apurbo = Shop('age purbo chilam')
apurbo.add_to_cart('chiruni')
print(apurbo.cart)
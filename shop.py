class Shop:

    cart = []
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
            self.cart.append(item)


mehzbeeeen = Shop('meh jabeeen')
mehzbeeeen.add_to_cart('shoes')
mehzbeeeen.add_to_cart('phones')         
print(mehzbeeeen.cart)   

nisho = Shop('noiso')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)
class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
        #homework
    def remove_item(self,product):
        for item in self.cart:
            if item['item'] == product:
                self.cart.remove(item)

                


    def checkout(self,amount):
        total =0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price',total)    
        if amount < total:
            print(f'please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')    
                   


Swanpan =Shopping('Al AN SHOPAN')
Swanpan.add_to_cart('alu',50,6)
Swanpan.add_to_cart('dim',12,24)
Swanpan.add_to_cart('rice',50,5)

print(Swanpan.cart)
Swanpan.remove_item('rice')
print(Swanpan.cart)
# Swanpan.checkout(600)
# Swanpan.checkout(1600)

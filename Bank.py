# class Bank:
#     def __init__(self,balance):
#         self.balance = balance
#         self.min_withdraw = 100
#         self.max_withdraw = 100000


#     def get_balance(self):
#         return self.balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount

#     def withdraw(self,amount):
#         if amount <self.min_withdraw:
#             print( f'fokira.you can not withdraw below {self.min_withdraw}')
#         elif amount> self.max_withdraw:
#             print( f'bank fokir hoye jabe.you can not withdraw more than {self.max_withdraw}')   
#         else:
#             self.balance -= amount
#             print( f'Here is your money {amount}')
#             print(f'your balance after withdraw {self.get_balance()}')


# Brac = Bank(15000)
# Brac.withdraw(25)
# Brac.withdraw(500000000)      
# Brac.withdraw(1000)   

# dbbl = Bank(5000)
# dbbl.deposit(2000)
# dbbl.deposit(2000)
# print(dbbl.get_balance())
#-----------------------------
# class Bank:
#     def __init__(self,balance):
#         self.balance = balance
#         self.min_withdraw = 200
#         self.max_withdraw = 3000

#     def get_balance(self):
#         return self.balance
    
#     def deposit(self,amount):
#         if amount > 0 :
#             self.balance += amount

#     def withdraw(self,amount):
#         if amount < self.min_withdraw:
#             print(f'you can not withdraw less than {self.min_withdraw}')
#         elif amount > self.max_withdraw:
#             print(f'fokira bank fokir hoea jabe.you can\'t with draw more than {self.max_withdraw}')    

#         else:
#             self.balance -= amount
#             print(f'Here is your money {amount}')
#             print(f'Your balance after withdraw { self.get_balance()}')


# SIBL = Bank(5000)
# # SIBL.withdraw(100)
# #SIBL.withdraw(6000)
# #SIBL.withdraw(3000)
# SIBL.deposit(2000)
# # total=SIBL.get_balance()
# # print(total) 
# print(SIBL.get_balance()) 
#-----------------------------
class Bikash:
    def __init__(self,balance,max,min):
        self.balance = balance
        self.max_withdraw = max
        self.min_withdraw = min

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
          self.balance += amount
        
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'Fokira! you can\'t withdraw less than {self.min_withdraw}')

        elif amount > self.max_withdraw:
            print(f'Oh no! bank Fokir hoea jabe.you can withdraw more than {self.max_withdraw}')

        else:
            self.balance -= amount
            print(f'Here is your amount {amount}')
            print(f'Your balance after withdraw {self.get_balance()}')

Brak = Bikash(5000,3000,1000)
print(Brak.get_balance())
# Brak.withdraw(500)
# Brak.withdraw(3000)
# Brak.withdraw(6000)
Brak.deposit(4000)
print(Brak.get_balance())

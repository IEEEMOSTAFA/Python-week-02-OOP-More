# encapsulation  ----> hide details
# access modifiers:: public,protected,private


# class Bank:
#     def __init__(self,holder_name,initial_deposit) -> None:
#         self.holder_name = holder_name # public attribute 
#         self._branch = 'banani 11' #protected-- # ekta under score mane protected na .kintu onek a etake protected bollar chesta kore-->kinto kono rule nei
#         self.balance = initial_deposit
#         self.__balance = initial_deposit #private----


#     def deposit(self,amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
#       #class er bitor theke access korte pari bole atake bole private


#     def withdraw(self,amount):
#         if amount < self.__balance:
#             self.__balance = self.__balance - amount
#             return amount

#         else:
#             return f'Fokira taka nai'  
        


# rafsan = Bank('Chooto bro',10000)
# print(rafsan.holder_name)
# rafsan.holder_name = 'boro vai'
# # print(rafsan.holder_name)
# rafsan.deposit(40000)
# print(rafsan.get_balance())
# print(rafsan.holder_name)
# # print(rafsan._branch)
# # print(dir(rafsan))
# print(rafsan._Bank__balance)

#------------------------------------

class Bank:

    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name
        self._branch = 'Banani 11'
        self.balance = initial_deposit
        self.__balance = initial_deposit
    
    def deposit(self,amount):
        
        self.__balance +=  amount

    def get_balance(self):
        return self.__balance


    def withdraw(self,amount):

        if amount < self.__balance:
            self.__balance = self.__balance - amount

            return amount
        else:
            return f'Fokira Taka Nai'
        

rafsan = Bank('Chotto bro',10000)
# print(rafsan.holder_name)
# print(rafsan.balance)
# rafsan.holder_name = 'boro bhai'
# print(rafsan.holder_name)        
rafsan.deposit(40000)
print(rafsan.get_balance())

print(rafsan._branch)

# print(dir(rafsan))

def call():
    print("calling someone i don't know ")
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features =['camera','speaker','hamer']


    def call(self):
        print("calling one person")
    def send_sms(self,phone,sms):
        text = f'sending SMS to:{phone} and message:{sms}'
        return text 
my_phone = Phone()
print(my_phone.features)
my_phone.call()    
# my_phone.send_sms (41524,'I forgot to miss you')    
result = my_phone.send_sms (41524,'I forgot to miss you')
print(result)

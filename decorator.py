
"""  
def timer(func):
    def inner():
        print('time started')
        # print(func)
        func()
        print('time ended')

    return inner
# timer()()


#Easier way to decorated
@timer
def get_factorial():
    print('Factorial Starting')

get_factorial()

#vajailla way to decorated
# timer(get_factorial)()

 """
import math
import time
def timer(func):
    def inner(*args,**kwargs):
        print('time started')
        start = time.time()
        func(*args,**kwargs)  # chaile key oala args o dite pari  --------(**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time taken {end - start}')
    return inner
#Easier way to decorated
@timer
def get_factorial(n): # jodi inner function a kice dite chai
    print('Factorial Starting')
    result = math.factorial(n)
    print(f'factorial of {n} is : {result}')

get_factorial(n=12)







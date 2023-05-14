import datetime
import math as my_math
from functools import reduce
def my_wrapper(func):
    def wrapper(arg):
        print(f"Sup {arg}")
        func(arg)
        print(f"Adios {arg}")
    return wrapper

@my_wrapper
def hallan_ami(name):
    print("hi")
    return 'my name is ' + name

hallan_ami("James")


my_bd = 1988

current_date = datetime.date.today()
age = current_date.year - my_bd
current_month = current_date.month
print(age)
print(current_month)


lis_t = [1, 2, 3, 4, 5, 6]
print(reduce(lambda x, y: x*y, lis_t))
print(my_math.prod(lis_t))


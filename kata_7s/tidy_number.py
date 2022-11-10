# Definition
#
# A Tidy number is a number whose digits are in non-decreasing order.
#
# Task
#
# Given a number, Find if it is Tidy or not .

def tidyNumber(n):
    new_nu = 0
    for num in str(n):
        if new_nu > int(num):
            return False
        else:
            new_nu = int(num)
    return True

def tidyNumber2(n):
    number = int(str(n)[0])
    for num in str(n):
        if int(num) < number:
            return False
        else:
            number = int(num)
    return True
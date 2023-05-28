# Definition
#
# Strong number is the number that the sum of the factorial of its digits is equal to number itself.
#
# For example, 145 is strong, since 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Task
#
# Given a number, Find if it is Strong or not and return either "STRONG!!!!" or "Not Strong !!".
#
# Notes
#
# Number passed is always Positive.
# Return the result as String

def strong_num(number):
    num = 0

    for char in str(number):

        num2 = 1

        for char2 in range(1, int(char) + 1):
            num2 *= char2

        num += num2

    return "STRONG!!!!" if num == number else "Not Strong !!"

#not using str()
def strong_num2(number):
    temp_number = number
    num = 0

    while number > 0:

        temp = number % 10
        temp2 = 1

        for char in range(1, temp + 1):
            temp2 *= char

        num += temp2

        number //= 10

    return 'STRONG!!!!' if num == temp_number else 'Not Strong !!'
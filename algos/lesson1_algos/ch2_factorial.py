# factorial 1 * 2 * 3 * 4 * 5al of 5 = !5:
#

# factorial of 4 = !4
# 1 * 2 * 3 * 4

# usually factorial questions don't include negative aka Gamma-functions
# math.factorial()

# https://www.codewars.com/kata/5a4d303f880385399b000001



































# def strong_num2(number):
#     temp_number = number
#     num = 0
#
#     while number > 0:
#
#         temp = number % 10
#         temp2 = 1
#
#         for char in range(1, temp + 1):
#             temp2 *= char
#
#         num += temp2
#
#         number //= 10
#
#     return 'STRONG!!!!' if num == temp_number else 'Not Strong !!'
#
#
# from math import factorial
#
#
# strong_num3 = lambda n: ["Not Strong !!", "STRONG!!!!"][n == sum(factorial(int(d)) for d in str(n))]
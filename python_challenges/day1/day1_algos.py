# User inputs two numbers. One number is assigned to a variable, the other number is assigned to b variable.
# The task is to invert the variables, so that the first variable contains the second number, while the
# first number is in the second variable.
from math import factorial

# simple way
a = 10
b = 20
a, b = b, a
print(a, b)

# math
a = a + b
a = a - b
b = a - b
print(a, b)



# When User enters a number, its factorial is displayed. 5!

my_factorial = 1

for num in range(1, 5+1):
    my_factorial *= num
print(my_factorial)
print(factorial(5))


# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.

# converting to string
my_num = 349
my_sum = 0
for num in str(my_num):
    my_sum += int(num)
print(my_sum)

# without str wrapping
once = my_num % 10
print(once)
my_num = my_num // 10
print(my_num)
tens = my_num % 10
print(tens)
hund = my_num // 10
print(hund)
print(once + tens + hund)
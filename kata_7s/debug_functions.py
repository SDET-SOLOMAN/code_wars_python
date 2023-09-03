# Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits.
# Assume that argument is an integer.
#
# Example
#
# 123  => 6
# 223  => 7
# 1337 => 14

# given broken function:

# def get_sum_of_digits(num):
#     sum = None
#     digits = list(num)
#     for x in digits:
#         sum + x
#     return sum

def get_sum_of_digits(num):
    sum = 0
    digits = list(int(x) for x in str(num))
    for x in digits:
        sum += x
    return sum


def get_sum_of_digits2(num):
    return sum(map(int, str(num)))


get_sum_of_digits3 = lambda num: sum(int(x) for x in str(num))

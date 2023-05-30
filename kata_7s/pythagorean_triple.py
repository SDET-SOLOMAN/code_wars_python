# Given an unsorted array of 3 positive integers [ n1, n2, n3 ], determine if it is possible
# to form a Pythagorean Triple using those 3 integers.
#
# A Pythagorean Triple consists of arranging 3 integers, such that:
#
# a2 + b2 = c2
#
# Examples
#
# [5, 3, 4] : it is possible to form a Pythagorean Triple using these 3 integers: 32 + 42 = 52
#
# [3, 4, 5] : it is possible to form a Pythagorean Triple using these 3 integers: 32 + 42 = 52
#
# [13, 12, 5] : it is possible to form a Pythagorean Triple using these 3 integers: 52 + 122 = 132
#
# [100, 3, 999] : it is NOT possible to form a Pythagorean Triple using these 3 integers -
# no matter how you arrange them, you will never find a way to satisfy the equation a2 + b2 = c2
#
# Return Values
#
# For Python: return True or False
# For JavaScript: return true or false
# Other languages: return 1 or 0 or refer to Sample Tests.


# long way not using methods
def pythagorean_triple(integers):
    low_num1 = integers[0]

    for char in integers:

        if char < low_num1:
            low_num1 = char

    integers.remove(low_num1)

    low_num2 = integers[0]

    for char in integers:
        if char < low_num2:
            low_num2 = char

    integers.remove(low_num2)

    return integers[0] ** 2 == low_num1 ** 2 + low_num2 ** 2


# short way:

def pythagorean_triple2(integers):
    integers.sort()
    return integers[2] ** 2 == integers[0] ** 2 + integers[1] ** 2


def pythagorean_triple3(integers):
    min1, min2, max_num = sorted(integers)
    return min1 ** 2 + min2 ** 2 == max_num ** 2

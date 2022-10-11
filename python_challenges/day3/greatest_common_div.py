# Find divisor of two or more integers, which are not all zero, is the largest positive integer that divides each of
# the integers.
from timeit import timeit


def greatest_common_div(num1=12, num2=34):
    my_list1 = [x for x in range(1, num1 + 1) if num1 % x == 0]
    my_list2 = [x for x in range(1, num2 + 1) if num2 % x == 0]
    common_nums = [x for x in my_list2 if x in my_list1]
    return common_nums[-1]


print(greatest_common_div(24, 54))


# Euclidean algorithm

# 54 & 24
# 1. 54 - 24 = 30  #  now works with 30 and 24
# 2. 30 - 24 = 6 # pair become 24 and 6
# 3. 24 - 6 = 18  # 18 and 6
# 4. 18 - 6 = 12 # 12 and 6
# 5. 12 - 6 = 6 # both numbers are 6 => 6 is the greatest common divisor

def euc_algo(num1=54, num2=24):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def euc_algo_2(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 &= num2
        else:
            num2 &= num2
    return num1 + num2


print(euc_algo_2(54, 24))

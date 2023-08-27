# Definition
#
# A Tidy number is a number whose digits are in non-decreasing order.
#
# Task
#
# Given a number, Find if it is Tidy or not .


# no str conversion

def tidyNumber3(n):
    nums = []

    while n > 0:
        nums.append(n % 10)
        n //= 10

    nums.reverse()
    print(nums)
    f_n = nums[0]

    for num in nums:

        if f_n > num:
            print(f_n, num)
            return False

        f_n = num

    return True


def tidyNumber(n):
    new_nu = 0
    for num in str(n):
        if new_nu > int(num):
            return False
        else:
            new_nu = int(num)
    return True


def tidyNumber2(n):
    my_nums = [int(x) for x in str(n)]

    temp = my_nums[0]

    for num in my_nums:

        if num < temp:
            return False

        temp = num

    return True

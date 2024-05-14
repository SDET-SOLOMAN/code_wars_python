# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    my_list = [str(num) for num in str(num)]
    new_list = []
    for num in my_list:
        new_list.append(str((int(num)) ** 2))
    return int("".join(new_list))


def square_digits2(num):
    my_sol = ""
    if num <= 0:
        return 0
    for nums in str(num):
        my_sol += str(int(nums) ** 2)
    return int(my_sol)


#------
# using map and funcs

s = lambda x: str(int(x) ** 2)


def another_func(x):
    if not x or x <= 0:
        return [0]

    s = []

    while x > 0:
        s.append(x % 10)
        x //= 10
    return s[::-1]


def square_digits3(num):
    return int(''.join(map(s, another_func(num))))

#-------------------------------
def square_digits4(num):
    return int(''.join([str(int(x) * int(x)) for x in str(num)]))

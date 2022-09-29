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


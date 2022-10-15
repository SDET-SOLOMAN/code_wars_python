# Complete the function which takes two arguments and returns all numbers which are divisible
# by the given divisor. First argument is an array of numbers and the second is the divisor.

# [1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]


def divisible_by2(numbers, divisor):
    my_list = []
    for num in numbers:
        if num % divisor == 0:
            my_list.append(num)
    return my_list


def divisible_by3(n, d):
    return list(filter(lambda x: not x % d, n))

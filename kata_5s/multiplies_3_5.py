# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
#
# Courtesy of projecteuler.net (Problem 1)

from functools import reduce

def solution(number):
    return sum(x for x in range(1, number) if x % 3 == 0 or x % 5 == 0)

solution2 = lambda combo: reduce(lambda x, y: x + y,
                                [x for x in range(1, combo) if x % 3 == 0 or x % 5 == 0]) if combo > 3 else 0


def solution3(number):
    my_sum = 0

    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            my_sum += num

    return my_sum


from functools import reduce
def solution4(number):
    num = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number)))

    return reduce(lambda x, y: x + y, num) if len(num) >= 2 else 0

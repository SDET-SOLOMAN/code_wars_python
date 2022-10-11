# div of a num, besides the num itself == num

from python_challenges.day3.amicable_nums import get_divs


def is_perfect(num):
    return num == sum(get_divs(num, False))


print(is_perfect(8))

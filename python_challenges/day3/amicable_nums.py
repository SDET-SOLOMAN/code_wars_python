# Check if two numbers are friendly to each other or not.
#
# Amicable number:
# n1 sum of divisors (except an n1) are equal to n2 and sum of divisors n2 are equal to n1.
# For example: 220 and 284
# 220: divisors [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
# 284: divisors [1, 2, 4, 71, 142]


def get_divs(num, include_num: bool):
    result = []
    if include_num:
        needed_range = range(1, num + 1)
    else:
        needed_range = range(1, num)

    for item in needed_range:
        if num % item == 0:
            result.append(item)
    return result


def is_amicable(num1, num2):
    div_num1 = get_divs(num1, False)
    div_num2 = get_divs(num2, False)

    return num1 == sum(div_num2) and num2 == sum(div_num1)

print(is_amicable(220, 284))
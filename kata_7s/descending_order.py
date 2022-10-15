# Your task is to make a function that can take any non-negative integer as an argument and return
# it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    name = (list(str(num)))
    name.sort()
    return int("".join(name)[::-1])


def descending_order2(num):
    num = int(''.join(sorted([x for x in str(num)], reverse=True)))
    return num


def descending_order3(num):
    return int(''.join(str(x) for x in sorted([int(s) for s in str(num)], reverse=True)))

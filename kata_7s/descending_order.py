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


def descending_order4(num):
    a = sorted([int(x) for x in str(num)], reverse=True)
    return int(''.join(str(x) for x in a))


# ------ using multiple functions

def list_maker(x):
    s = []

    while x > 0:
        s.append(x % 10)
        x //= 10

    return s


string_maker = lambda x: map(str, sorted(list_maker(x), reverse=True))


def descending_order5(num):
    if not num or num <= 0:
        return 0

    return int(''.join(string_maker(num)))

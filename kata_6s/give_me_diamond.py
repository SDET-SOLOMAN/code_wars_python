# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James.
# Since James doesn't know how to make this happen, he needs your help.
#
# Task
#
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*)
# characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#
# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of
# even or negative size.
#
# Examples
#
# A size 3 diamond:
#
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"
#
# A size 5 diamond:
#
#   *
#  ***
# *****
#  ***
#   *
# ...that is:
#
# "  *\n ***\n*****\n ***\n  *\n"

def diamond(n):
    if n % 2 != 0 and n >= 1:
        a = ''.join(" " * ((n - x) // 2) + '*' * (x) + '\n' for x in range(1, n + 1, 2))
        a += ''.join(" " * ((n - x) // 2) + '*' * (x) + '\n' for x in range(n - 2, -1, -2))
        return a
    return None

# Not my solution, but pretty cool:
def diamond2(n):
    exception = (n % 2 == 0 or n <= 0)
    return {True: None}.get(exception, make_diamond(n))


def make_diamond(n):
    asc = [(int((n - i) / 2) * ' ') + (i * '*' + '\n') for i in range(1, n + 1) if i % 2 == 1]
    desc = asc[::-1][1:]
    return ''.join(asc + desc)

# -----------------------


def diamond3(n):
    if n <= 0 or n % 2 == 0:
        return None

    diamond = ""

    for char in range(1, n + 1, 2):
        diamond += " " * ((n - char) // 2)
        diamond += "*" * char
        diamond += '\n'
    for char in range(n - 2, 0, -2):
        diamond += " " * ((n - char) // 2)
        diamond += "*" * char
        diamond += '\n'
    return diamond
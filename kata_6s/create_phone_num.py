# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of
# those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    first_nums = ''.join(str(x) for x in n[:3])
    middle = ''.join(str(x) for x in n[3:6])
    last = ''.join(str(x) for x in n[6:])
    return f"({first_nums}) {middle}-{last}"


def create_phone_number2(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


def create_phone_number3(n):
    n = ''.join(str(x) for x in n)
    n1, n2, n3 = n[:3], n[3:6], n[6:]
    return f"({n1}) {n2}-{n3}"
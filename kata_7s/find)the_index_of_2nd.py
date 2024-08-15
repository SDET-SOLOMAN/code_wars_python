# In this kata, you need to write a function that takes a string and a letter as input and
# then returns the index of the second occurrence of that letter in the string. If there is
# no such letter in the string, then the function should return -1. If the letter occurs only
# once in the string, then -1 should also be returned.
#
# Examples:
#
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1
# Good luck ;) And don't forget to rate this Kata if you liked it.

def second_symbol(s, symbol):
    if not s or symbol not in s or s.lower().count(symbol.lower()) <= 1:
        return -1
    new_s = [i for i, x in enumerate(s) if symbol == x in s[:i]]
    return new_s[0] if new_s else -1


def second_symbol2(s, x):
    if not s or s.count(x) <= 1:
        return -1
    return s.find(x, s.find(x) + 1)
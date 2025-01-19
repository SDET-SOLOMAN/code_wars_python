# Given a mixed array of number and string representations of integers, add up the non-string
# integers and subtract the total of the string integers.
#
# Return as a number.

def div_con(s):
    return sum(num if type(num) == int else -int(num) for num in s)


s = lambda x: -abs(int(x))
def div_con2(x):
    return sum(s(num) if type(num) == str else num for num in x)
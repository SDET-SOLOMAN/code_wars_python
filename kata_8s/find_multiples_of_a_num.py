# In this simple exercise, you will build a program that takes a value, integer , and returns a list of
# its multiples up to another value, limit . If limit is a multiple of integer, it should be included as
# well. There will only ever be positive integers passed into the function, not consisting of 0. The limit
# will always be higher than the base.
#
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6
# are the multiples of 2 up to 6.


def find_multiples(integer, limit):
    return [x for x in range(integer, limit + 1) if x % integer == 0]


def find_multiples2(i, l):
    return list(filter(lambda x: x % i == 0, range(i, l + 1)))
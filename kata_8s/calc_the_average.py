# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.

def find_average(n):
    if not n:
        return 0
    return sum(n) / len(n)


def find_average2(n):
    try:
        return sum(n) / len(n)
    except ZeroDivisionError:
        return 0
# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    if number >= 0:
        return -number
    return abs(number)
    # return number * -1
    # return -number

# Complete the method so that it'll find the greatest product of five consecutive digits in the given string of digits.

# For example: the greatest product of five consecutive digits in the string "123834539327238239583" is 3240.

# The input string always has more than five digits.

# Adapted from Project Euler.

def greatest_product(st: str) -> int:
    
    mx = 0
    
    for i in range(len(st) - 4):
        c = 1
        for ch in st[i:i+5]:
            c *= int(ch)
        if c > mx:
            mx = c
    return mx

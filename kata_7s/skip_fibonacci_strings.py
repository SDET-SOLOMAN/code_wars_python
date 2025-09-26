# Description:
# Given that

# f0 = '0'
# f1 = '01'
# f2 = '010' = f1 + f0
# f3 = '01001' = f2 + f1
# You will be given a number and your task is to return the nth fibonacci string. For example:

# solve(2) = '010'
# solve(3) = '01001'
# More examples in test cases. Good luck!

# If you like sequence Katas, you will enjoy this Kata: Simple Prime Streaming

def solve(n):
    
    f = "0"
    f1 = "01"
    
    if n < 2:
        return [f, f1][n]
    
    for num in range(n -1):
        temp = f1
        f1 = f1 + f
        f = temp
    return f1


def solve2(n):
    
    first = "0"
    second = "01"
    
    if n < 2:
        return [first, second][n]
    for num in range(n - 1):
        first, second = second, second + first
    return second



def validBraces(s: str) -> bool:

    s = ''.join(ch for ch in s if ch in '()[]{}')

    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    return len(s) == 0

print(validBraces("(123 [asdsa!312](2*{adada}/10){{[]}})"))
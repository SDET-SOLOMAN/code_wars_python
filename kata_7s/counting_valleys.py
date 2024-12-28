# Start is always from zero level.
#
# Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level
# from valley counts as an exit of a valley.
#
# One passed valley is equal one entry and one exit of a valley.
#
# s='FUFFDDFDUDFUFUF'
# U=UP
# F=FORWARD
# D=DOWN
# To represent string above
#
# (level 1)  __
# (level 0)_/  \         _(exit we are again on level 0)
# (entry-1)     \_     _/
# (level-2)       \/\_/

def counting_valleys(s):
    
    m = 0
    t = 0

    for char in s:
        if m == -1 and char == 'U':
            t += 1
        if char == 'D':
            m -= 1
        elif char == 'U':
            m += 1
    return t


def counting_valleys2(s):
    x = 0
    t = 0

    for char in s:

        if char == "U":
            if x == -1:
                t += 1
            x += 1

        elif char == "D":
            x -= 1

    return t


def counting_valleys3(s):
    step = 0
    total = 0
    d = {"U": 1, "D": -1}

    for char in s:

        if d.get(char):
            if step == -1 and d[char] == 1:
                total += 1
            step += d[char]

    return total
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
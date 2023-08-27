# Given a string made up of letters a, b, and/or c, switch the position of letters a and b
# (change a to b and vice versa). Leave any incidence of c untouched.
#
# Example:
#
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    new_s = ''
    for char in s:
        if char == 'a':
            new_s += 'b'
        elif char == 'b':
            new_s += 'a'
        else:
            new_s += 'c'
    return new_s


switcheroo2 = lambda x: ''.join('b' if s == 'a' else 'a' if s == 'b' else s for s in x)

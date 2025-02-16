# DESCRIPTION:
#
# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
#
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# simple one line using lambda

solution = lambda s: ''.join(x if x.islower() else " " + x for x in s)


def solution2(s):
    new_s = ""
    for n in s:
        if n.isupper():
            new_s += " " + n
        else:
            new_s += n
    return new_s


def solution3(s):
    return "".join(x if x.islower() else f" {x}" for x in s)
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


def switcheroo3(s):
    d = {
        'a': 'b',
        'b': 'a'
    }
    return ''.join(d[x] if d.get(x) else x for x in s)


def switcheroo4(s):
    return s.replace("a", "1").replace("b", "2").replace('1', "b").replace("2", "a")


def swi(x):
    match x.lower():
        case "b":
            return "a"
        case "a":
            return "b"
        case _:
            return x

def switcheroo5(s):
    return "".join(swi(x) for x in s)


def switcheroo6(s):
    x = {
        "a": "b",
        "b": "a"
    }

    return "".join(x.get(l, l) for l in s)

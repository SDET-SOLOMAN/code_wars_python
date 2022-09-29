# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")


def no_space2(x):
    new_string = ""
    for char in x:
        if char != " ":
            new_string += char
    return new_string


no_space3 = lambda x: ''.join(x.split())

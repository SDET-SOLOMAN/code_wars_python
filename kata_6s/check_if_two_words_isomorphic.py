# Two strings a and b are called isomorphic if there is a one to one mapping possible for every character of a to every
# character of b. And all occurrences of every character in a map to same character in b.
#
# Task
#
# In this kata you will create a function that return True if two given strings are isomorphic to each other, and
# False otherwise. Remember that order is important.
#
# Your solution must be able to handle words with more than 10 characters.
#
# Example
#
# True:
#
# CBAABC DEFFED
# XXX YYY
# RAMBUNCTIOUSLY THERMODYNAMICS
# False:
#
# AB CC
# XXY XYY
# ABAB CD

def isomorph(a, b):
    if len(a) != len(b):
        return False

    a1 = {}
    a2 = {}

    for i, char in enumerate(a):
        if char not in a1:
            a1[char] = b[i]
            a2[char] = 1
        else:
            if a1[char] != b[i]:
                return False
            else:
                a2[char] += 1
    b1 = {}
    b2 = {}

    for i, char in enumerate(b):
        if char not in b1:
            b1[char] = a[i]
            b2[char] = 1
        else:
            if b1[char] != a[i]:
                return False
            else:
                b2[char] += 1

    for k, v in a1.items():
        if k != b1[v] and a2[k] != b2[v]:
            return False
    return True

# found on codewars:
def isomorph(a, b):
    print(a)
    print([a.index(x) for x in a])
    return [a.index(x) for x in a] == [b.index(x) for x in b]
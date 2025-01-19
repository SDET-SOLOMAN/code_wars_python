# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    # The function code should be here
    return {k: s.count(k) for k in s}


def count2(string):
    c = {}
    for char in string:
        c[char] = c.get(char, 0) + 1
    return c


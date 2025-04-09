# Find the first character that repeats in a String and return that character.
#
# first_dup('tweet') => 't'
# first_dup('like') => None
# This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.
#
# Another example:
#
# In 'translator' you should return 't', not 'a'.
#
# v      v
# translator
#   ^   ^
# While second 'a' appears before second 't', the first 't' is before the first 'a'.

def first_dup(s):
    d = {k: s.count(k) for k in s}

    for k, v in d.items():
        if v > 1:
            return k
    return None
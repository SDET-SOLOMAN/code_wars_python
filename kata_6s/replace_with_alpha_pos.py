# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
#
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

import string


def alphabet_position(text):
    if not text:
        return ""
    alpha = string.ascii_lowercase
    return ' '.join(str(alpha.index(x) + 1) for x in text.lower() if x in alpha)


from string import ascii_lowercase

alpha = ascii_lowercase

find_letter = lambda x: str(alpha.index(x) + 1)


def alphabet_position2(text):
    text = text.lower().split()

    return " ".join(" ".join(find_letter(x) for x in s if x.isalpha()) for s in text)

# found this ord solutions
def alphabet_position3(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
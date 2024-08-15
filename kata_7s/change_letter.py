# When provided with a String, capitalize all vowels
#
# For example:
#
# Input : "Hello World!"
#
# Output : "HEllO WOrld!"
#
# Note: Y is not a vowel in this kata.

is_vowel = lambda x: x in "iouiae"


def swap(st):
    return "".join(x.upper() if is_vowel(x.lower()) else x for x in st)
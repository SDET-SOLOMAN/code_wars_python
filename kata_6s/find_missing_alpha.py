# Find the missing letter
#
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the
# missing letter in the array.
#
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.
#
# Example:
#
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)

import string


def find_missing_letter(chars):
    alphab = list(string.ascii_lowercase)
    chars2 = [x.lower() for x in chars]
    index_of_alphas = alphab.index(chars[0].lower())
    index_of_chars = 0
    while index_of_alphas <= 25:
        print(alphab[index_of_alphas])
        print(chars2[index_of_chars])
        if alphab[index_of_alphas] != chars2[index_of_chars]:
            if chars[index_of_chars].isupper():
                return alphab[index_of_alphas].upper()
            return alphab[index_of_alphas]
        index_of_chars += 1
        index_of_alphas += 1


def find_missing_letter2(chars):
    first = ord(chars[0])
    for char in chars:
        if ord(char) != first:
            return chr((first))
        first += 1
    return ""


from string import ascii_lowercase, ascii_uppercase


def find_missing_letter3(chars):
    a = list(ascii_lowercase + ascii_uppercase)

    a_index = a.index(chars[0])

    for char in chars:
        if a[a_index] != char:
            return a[a_index]
        a_index += 1

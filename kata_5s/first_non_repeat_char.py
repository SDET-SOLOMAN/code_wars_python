# Write a function named first_non_repeating_letter that takes a string input, and returns the first character
# that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once
# in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should
# return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    string2 = string.lower()
    word = ''.join(char if string.upper().count(char.upper()) == 1 or string2.count(char) == 1
                   else '' for char in string)
    print(word)
    if len(word) >= 1:
        return word[0]
    return ''


# nott using count

def first_non_repeating_letter2(string):
    my_dict = {

    }

    str1 = string.lower()

    for char in str1:
        if my_dict.get(char):
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    print(my_dict)

    for char in string:
        if my_dict[char.lower()] == 1:
            return char
    return ""


def first_non_repeating_letter3(s):
    s2 = s.lower()
    for index, char in enumerate(s2):
        if char not in s2[index + 1:] and char not in s2[:index]:
            return s[index]
    return ""


def first_non_repeating_letter4(string):
    for index, letter in enumerate(string):
        if string.lower().count(letter.lower()) == 1:
            return string[index]
    return ""


def first_non_repeating_letter5(string):
    print(string)

    d = {k: string.lower().count(k.lower()) for k in string}

    for k, v in d.items():
        if v == 1:
            return k
    return ""
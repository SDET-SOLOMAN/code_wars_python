# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
#
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if not text:
        return ""
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = text.split()
    new_s = text[0]

    for char in text[1:]:
        new_s += char.capitalize()
    return new_s


import re


def to_camel_case2(text):
    if text == '':
        return ""
    new_string = re.split("(-|_|\s)\s*", text)
    new_word = new_string[0]
    for num in new_string[1:]:
        if num != '_' and num != '-':
            new_word += num[0].upper()
            new_word += num[1:]
    return new_word

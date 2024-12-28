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

def to_camel_case3(text):
    if not text:
        return ""
    chars = ["_", "-"]
    text = ''.join(" " if x in chars else x for x in text)
    text = text.split()
    new_s = text[0]

    for char in text[1:]:
        new_s += char.capitalize()
    return new_s


def to_camel_case5(text):
    if not text:
        return ""
    rep1 = text.replace("_", "-")
    text1 = rep1.split("-")
    print(text1)
    return text1[0] + ''.join(x.capitalize() for x in text1[1:] if x.isalpha() and x != '-')


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

# not using replace or split:

def to_camel_case4(text):
    if not text:
        return ""

    new_s = ""
    turn_upper = False

    for char in text:
        if char.isalpha():
            if turn_upper:
                new_s += char.upper()
                turn_upper = False
            else:
                new_s += char
        else:
            turn_upper = True
    return new_s


def to_camel_cas5e(text):
    if not text:
        return ""

    # text = text.replace("_", "-").replace("-", " ").split()

    tex = []
    temp = ""

    for i, char in enumerate(text):
        if char != "_" and char != "-":
            temp += char
        if char == "_" or char == "-" or (i == len(text) - 1 and temp):
            tex.append(temp)
            temp = ""
    return tex[0] + ''.join(x.capitalize() for x in tex[1:])


def to_camel_case6(text):
    text = text.replace("_", "-").replace("-", " ").split()

    return text[0] + ''.join(x.capitalize() for x in text[1:]) if text else ""
# The goal of this exercise is to convert a string to a new string where each character in the new string is
# "(" if that character appears only once in the original string, or ")" if that character appears more than
# once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes
#
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
# the "XXX" is the expected result, not the input!


def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    for char in word:
        if word.count(char) > 1:
            new_string += ")"
        else:
            new_string += "("
    return new_string


def duplicate_encode2(word):
    word = word.lower()
    new_word = ""
    char_count = {}
    for char in word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in word:
        if char_count[char] > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word


def duplicate_encode3(word):
    my_dict = dict()
    word = word.lower()

    for char in word:
        if char in my_dict:
            my_dict[char] = ')'
        else:
            my_dict[char] = '('

    return ''.join(my_dict[char] for char in word)



def duplicate_encode4(word):
    word = word.lower()
    return ''.join(["(" if word.count(x) == 1 else ")" for x in word])
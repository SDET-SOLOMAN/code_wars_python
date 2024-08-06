# DESCRIPTION:
#
# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but
# frequently they can be guessed due to common cultural references. You can get your passphrases stronger
# by different means. One is the following:
#
# choose a text in capital letters including or not digits and non alphabetic characters,
#
# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.
# Example:
#
# your text: "BORN IN 2015!", shift 1
#
# 1 + 2 + 3 -> "CPSO JO 7984!"
#
# 4 "CpSo jO 7984!"
#
# 5 "!4897 Oj oSpC"
#
# With longer passphrases it's better to have a small and easy program. Would you write it?


import string


def play_pass(s, n):
    d_nums = {
        0: 9,
        1: 8,
        2: 7,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 1,
        9: 0
    }

    alphabet = string.ascii_lowercase + string.ascii_lowercase

    s = s.lower()

    new_word = ''

    for index, char in enumerate(s):

        if char.isdigit():
            new_word += str(d_nums.get(int(char)))

        elif char.isalpha():

            nn = alphabet.index(char)

            if index % 2 == 0:
                new_word += alphabet[n + nn].upper()

            else:
                new_word += alphabet[n + nn]
        else:
            new_word += char

    return_word = ''

    for char in range(len(new_word) - 1, - 1, -1):
        return_word += new_word[char]

    return return_word


al = string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase

play_pass2 = lambda s, n: ''.join(al[al.index(x) + n].upper() if x.isalpha() and i % 2 == 0
                                  else al[al.index(x) + n].lower() if x.isalpha() else str(
    9 - int(x) if x.isdigit() else x)
                                  for i, x in enumerate(s))[::-1]


def play_pass3(s, n):
    a = string.ascii_lowercase + string.ascii_lowercase
    numbers = {
        '0': '9',
        '1': '8',
        '2': '7',
        '3': '6',
        "4": '5',
        '5': '4',
        "6": '3',
        '7': '2',
        '8': '1',
        '9': '0'
    }
    s = s.lower()
    new_s = ""

    for char in range(0, len(s)):

        if char % 2 == 0:
            if s[char].isalpha():
                new_s += a[a.index(s[char]) + n].upper()
            elif s[char].isdigit():
                new_s += numbers.get(s[char])
            else:
                new_s += s[char]

        elif char % 2 != 0:
            if s[char].isalpha():
                new_s += a[a.index(s[char]) + n].lower()
            elif s[char].isdigit():
                new_s += numbers.get(s[char])
            else:
                new_s += s[char]
    return new_s[::-1]


import string


def play_pass2(s, n):
    alphabet = string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase
    new_word = ''

    for char in s:
        if char.isalpha():
            new_word += alphabet[alphabet.index(char) + n]
        elif char.isdigit():
            new_word += str(abs(9 - int(char)))
        else:
            new_word += char

    new_word_remix = ''.join(x.upper() if i % 2 == 0 else x.lower() for i, x in enumerate(new_word))

    new_s = ''

    for char in range(len(new_word_remix) - 1, -1, -1):
        new_s += new_word_remix[char]
    return new_s


al = string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase

play_pass3 = lambda s, n: ''.join(al[al.index(x) + n].upper() if x.isalpha() and i % 2 == 0 else al[
    al.index(x) + n].lower() if x.isalpha() else str(9 - int(x) if x.isdigit() else x) for i, x in enumerate(s))[::-1]

# using multiple functions

from string import ascii_lowercase

down_up = lambda x, s: x.upper() if s % 2 == 0 else x.lower()


def find_index(letter, n):
    alpha = ascii_lowercase + ascii_lowercase
    return alpha[alpha.index(letter) + n]


get_opposite_num = lambda x: str({0: 9, 1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0}[int(x)])


def play_pass4(s, n):
    s = s.lower()

    just_letters = "".join(
        down_up(find_index(letter, n), pos) if letter.isalpha() else letter for pos, letter in enumerate(s))[::-1]

    return "".join(x if not x.isdigit() else get_opposite_num(x) for x in just_letters)

# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.
import string


def high3(xx):
    alpha = string.ascii_lowercase

    word = ''
    max = 0

    for char in xx.split():
        temp = 0
        for letter in char:
            if letter in alpha:
                temp += alpha.index(letter) + 1
        if temp > max:
            max = temp
            word = char
    return word


def high(x):
    x = x.split(" ")
    alphabet = list(string.ascii_lowercase)
    my_dict = {alphabet[i]: i + 1 for i in range(0, len(alphabet))}
    score = 0
    score2 = 0
    word = ''
    for n in x:
        for s in n:
            score2 += my_dict[s]
        if score2 > score:
            word = n
            score = score2
        score2 = 0
    return word


# using ord() func ... found this through chatgpt solution
def high_v2(x):
    return max(x.split(), key=lambda val: sum(ord(y) - 96 for y in val))


import string


def high5(x):
    a = string.ascii_lowercase
    x = x.lower()

    word = ''
    score = 0

    temp_w = ""
    temp = 0

    for i, char in enumerate(x):
        if char != " ":
            temp_w += char
            temp += a.index(char) + 1
        if i == len(x) - 1 or char == " ":
            if temp > score:
                score = temp
                word = temp_w
            temp_w = ""
            temp = 0
    return word


import string


def hig6h(x):
    if not x:
        return ""

    nums = [x for x in range(1, 27)]

    alphas = string.ascii_lowercase

    letters = dict(zip(alphas, nums))

    temp_word = ""
    temp_score = 0

    final_word = ""
    final_score = 0

    for i, char in enumerate(x):

        if char != " ":
            temp_word += char
            temp_score += letters[char]

        if i == len(x) - 1 or char == " ":
            if temp_score > final_score:
                final_score = temp_score
                final_word = temp_word
            temp_word = ""
            temp_score = 0

    return final_word

# found this solution on codeWars
def high6(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


from string import ascii_lowercase

def word_score(s):
    n = 0
    alpha = ascii_lowercase
    d = {alpha[k]: k + 1 for k in range(len(alpha))}
    for char in s:
        n += d[char]
    return n


def high7(x):
    x = x.lower().split()
    m = ""
    score = -9999
    for char in x:
        temp = word_score(char)
        if temp > score:
            score = temp
            m = char
    return m


import string
a = string.ascii_lowercase
total = lambda x: sum(a.index(c) + 1 for c in x)
def high8(x):
    return max(x.split(), key=total)


word = lambda char: sum(ord(x) - 96 for x in char)
def high9(x):
    x = x.split()
    re = ("", 0)
    for char in x:
        temp = word(char)
        if temp > re[-1]:
            re = (char, temp)
    return re[0]
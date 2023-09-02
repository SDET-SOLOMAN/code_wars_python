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

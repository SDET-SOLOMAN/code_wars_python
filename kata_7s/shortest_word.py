# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    list_of = s.split(" ")
    min_word = list_of[0]
    for words in list_of:
        if len(words) < len(min_word):
            min_word = words

    return len(min_word)

def find_short2(s):
    return min(len(char) for char in s.split())
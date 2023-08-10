# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character. If the word's length is even, return
# the middle 2 characters.
#
# #Examples:

# Kata.getMiddle("test") should return "es"
#
# Kata.getMiddle("testing") should return "t"
#
# Kata.getMiddle("middle") should return "dd"
#
# Kata.getMiddle("A") should return "A"

get_middle = lambda word: ''.join(x for x in word[(len(word) // 2) - 1:
                                                  (len(word) // 2 + 1)]) if len(word) % 2 == 0 else \
                                                    word[(len(word) // 2)]


def get_middle2(s):
    len_s = len(s)
    middle = len(s) // 2

    return s[middle - 1] + s[middle] if len_s % 2 == 0 else s[middle]

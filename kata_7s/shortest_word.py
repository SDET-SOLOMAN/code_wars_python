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


def find_short3(s):
    return len(sorted(s.split(), key=len)[0])


def find_short4(s):
    length = 999999

    for char in s.split():

        temp = 0

        for c in char:
            temp += 1

        if temp < length:
            length = temp

    return length


def find_short5(s):
    return min(map(len, s.split()))


find_short6 = lambda words: len(sorted(words.split(), key=len)[0])
find_short8 = lambda words: sorted(map(len, s.split()))[0]


def find_short7(s):
    if not s:
        return 0

    s = s.split()
    min_w = len(s[0])

    for char in s[1:]:
        new_w = len(char)
        if new_w < min_w:
            min_w = new_w

    return min_w

# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.


def remove_char(s):
   return s[1:-1]

def remove_char2(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)

def remove_char3(s):
    num = len(s)
    if num <= 2:
        return ''
    return s[1:-1]


remove_char4 = lambda word: ''.join([word[x] for x in range(1, len(word) - 1)])


def remove_char5(s):
    new_s = ''
    for char in range(1, len(s) - 1):
        new_s += s[char]
    return new_s

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return ''.join(filter(lambda x: x != "!", s))


def remove_exclamation_marks2(s):
    return ''.join(x for x in s if x != '!')


def remove_exclamation_marks3(s):
    new_str = ''
    my_range = range(0,len(s))
    for char in my_range:
        if s[char] != "!":
            new_str += s[char]
    print(new_str)
    return new_str


remove_exclamation_marks4 = lambda word: ''.join(filter(lambda x: x != "!", word))


remove_exclamation_marks5 = lambda x: x.replace("!", "")
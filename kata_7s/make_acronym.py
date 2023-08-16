# Write function which takes a string and make an acronym of it.
#
# Rule of making acronym in this kata:
#
# split string to words by space char
# take every first letter from word in given string
# uppercase it
# join them toghether
# Eg:
#
# Code wars -> C, w -> C W -> CW
# Note: There will be at least two words in the given string!

def to_acronym(inp):
    my_words = ''
    for char in inp.split():
        my_words += char[0]
    return my_words.upper()


def to_acronym2(input):
    # only call upper() once
    return ''.join(word[0] for word in input.split()).upper()


# no split
def to_acronym3(inp):
    new_inp = ""
    status = True

    for char in inp:

        if status and char:
            new_inp += char.upper()
            status = False

        elif char == ' ':
            status = True

    return new_inp

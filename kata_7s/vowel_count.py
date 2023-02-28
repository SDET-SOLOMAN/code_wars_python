# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    counting = 0
    for letter in sentence:
        if letter in "aeiou":
            counting += 1
    return counting


# another way:

def get_count2(sentence):
    my_count = [x for x in sentence if x in 'aeiou']
    return len(my_count)


def get_count3(sentence):
    return len(list(filter(lambda x: x in 'aeiou', sentence)))


def get_count4(sentence):
    return sum(1 for x in sentence if x in 'aeiou')
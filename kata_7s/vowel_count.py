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

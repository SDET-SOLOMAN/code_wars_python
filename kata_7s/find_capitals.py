# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list
# containing the indexes of all capital letters in the string.
#
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]

def capitals(word):
    return [i for i, x in enumerate(word) if x.isupper()]


def capitals2(word):
    return list(filter(lambda x: word[x].isupper(), range(len(word))))
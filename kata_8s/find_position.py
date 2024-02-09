# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) - 96}"


def position2(alphabet):
    alpha = "abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1
    return f"Position of alphabet: {alpha}"
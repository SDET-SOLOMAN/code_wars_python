# Given a string of space separated words, return the longest word.
# If there are multiple longest words, return the rightmost longest word.
#
# Examples
# "red white blue"  =>  "white"
# "red blue gold"   =>  "gold"

def longest_word(s):
    return "".join(sorted(s.split(), key=len)[-1])
# Note: anagrams are case insensitive
#
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
#
# Examples
# "foefet" is an anagram of "toffee"
#
# "Buckethead" is an anagram of "DeathCubeK"

# write the function is_anagram
def is_anagram(test, original):
    test, original = test.lower(), original.lower()
    return all(original.count(x) >= test.count(x) for x in test) and len(original) == len(test)


# write the function is_anagram
def is_anagram2(test, original):
    test, original = test.lower(), original.lower()
    return sorted(test) == sorted(original)
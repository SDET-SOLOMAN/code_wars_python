# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
# For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a
# word and an array with words. You should return an array of all the anagrams or an empty array if
# there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]


anagrams_one_line = lambda word, words: list(filter(lambda x: sorted(x) == sorted(word), words))


def anagrams3(word, words):
    wordi = sorted([x for x in word])
    list1 = []
    for num in words:
        num1 = sorted([x for x in num])
        if ''.join(wordi) == "".join(num1):
            list1.append(num)
    return list1

# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be
# rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
#
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1, s2):
    return all(s2.count(x) <= s1.count(x) for x in set(s2))


def scramble3(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


def scramble2(s1, s2):
    dct = {x: s1.count(x) for x in set(s1)}

    for l in s2:
        if l not in dct or dct[l] < 1:
            return False
        dct[l] -= 1

    return True


def scramble4(s1, s2):
    s3 = {x: s1.count(x) for x in set(s1)}

    for char in s2:

        if not s3.get(char) or not s3[char] > 0:
            return False

        s3[char] -= 1

    return True
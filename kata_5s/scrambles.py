# Complete the function scramble(str1, str2) that returns true if a
# portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

scramble = lambda word1, word2: all(word1.count(s) >= word2.count(s) for s in set(word2))


def scramble2(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


def scramble3(s1, s2):
    s11 = {
        k: s1.count(k) for k in s1
    }

    s22 = {
        k: s1.count(k) for k in s2
    }

    for k, v in s22.items():
        if k not in s11 or s11[k] < v:
            return False
    return True

    # or
    # return all(v <= s11[k] if k in s11 else 0 for k, v in s22.items())


def scramble4(s1, s2):
    d = {x: s1.count(x) for x in set(s1)}

    for l in s2:
        if l not in d or d[l] < 1:
            return False
        d[l] -= 1

    return True
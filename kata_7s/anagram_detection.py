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
    return all(original.count(x) == test.count(x) for x in test) and len(original) == len(test)


# write the function is_anagram
def is_anagram2(test, original):
    test, original = test.lower(), original.lower()
    return sorted(test) == sorted(original)


# using dict

def is_anagram3(test, original):
    test = test.lower()
    org = original.lower()

    t = {k: test.count(k) for k in test}
    o = {k: org.count(k) for k in org}

    for k, v in o.items():
        if not t.get(k) or t[k] != v:
            return False

    for k, v in t.items():
        if not o.get(k) or o[k] != v:
            return False

    return True


make_d = lambda x: {k: x.count(k) for k in x}
def is_anagram4(t, o):
    tl, ol = len(t), len(o)

    if tl != ol:
        return False

    t = t.lower()
    o = o.lower()

    t = make_d(t)
    o = make_d(o)

    for k, v in t.items():
        if o.get(k, 0) != v:
            return False

    return True

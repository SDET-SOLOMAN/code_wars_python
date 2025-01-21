# vowelOne
#
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become
# 1's and non-vowels become 0's.
#
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
#
# Examples:
#
# vowelOne "abceios" -- "1001110"
#
# vowelOne "aeiou, abc" -- "1111100100"

def vowel_one(s):
    s = s.lower()
    v = "aeiou"

    return "".join(["0", "1"][x in v] for x in s)

def vowel_one2(s):
    s = s.lower()
    return ''.join(map(lambda x: '1' if x in 'aeiou' else '0', s))

def vowel_one3(s):
    s = s.lower()
    return ''.join(map(lambda x: ["0", "1"][x in "aioue"], s))


in_it = lambda x: x.lower() in "auioue"
def vowel_one4(s):
    d = {
        True: "1",
        False: "0"
    }
    return "".join(d[in_it(x)] for x in s)
    # return "".join(["0", "1"][in_it(x)] for x in s)
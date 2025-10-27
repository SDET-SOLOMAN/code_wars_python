# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a
# lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the
# length of the longest vowel substring. Vowels are any of aeiou.
#
# Good luck!
#
# If you like substring Katas, please try:

def solve(s):
    if not s:
        return 0

    v = "oeaui"
    s = s.lower()

    total = 0
    temp = 1

    for i, c in enumerate(s[:-1]):
        if c in v and s[i + 1] in v:
            temp += 1
        else:
            total = temp if temp > total else total
            temp = 1
    return total if total > temp else temp


import re

def solve2(s):
    return max(map(len, re.split(r'[^aeiou]+', s)))
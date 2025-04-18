# Write a method that takes a string as an argument and groups the number of time each character appears in the string as a hash sorted by the highest number of occurrences.
#
# The characters should be sorted alphabetically e.g:
#
# get_char_count("cba") == {1: ["a", "b", "c"]}
# You should ignore spaces, special characters and count uppercase letters as lowercase ones.
#
# For example:
#
# get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
# get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
# get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
# get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
# get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}


def get_char_count(s):
    s = s.lower()

    x = dict(sorted({k: s.count(k) for k in s if k.isalpha() or k.isdigit()}.items(), key=lambda n: n[1], reverse=True))
    print(x)

    re = {}

    for k, v in x.items():
        if v in re:
            re[v].append(k)
        else:
            re[v] = [k]

    for k, v in re.items():
        re[k] = sorted(v)
    return re
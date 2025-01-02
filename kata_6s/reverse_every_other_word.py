# Reverse every other word in a given string, then return the string. Throw away any leading or trailing
# whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be
# treated as if they are a part of the word in this kata.

def reverse_alternate(string):
    string = string.split()
    new_s = ''
    c = 0
    w_s = 0
    for num in string:
        if c % 2 == 0:
            new_s += num
            new_s += " "
        elif num != " ":
            new_s += num[::-1]
            new_s += " "
        c += 1
    return new_s[:-1]


reverse_alternate2 = lambda x: ' '.join(s if i % 2 == 0 else s[::-1] for i, s in enumerate(x.split()))


def reverse_alternate3(s):
    s = s.split()
    return ' '.join([x[::-1] if s.index(x) % 2 == 1 else x for x in s])


rev = lambda x, i: "".join(x[s] for s in range(-1, -len(x) -1, -1)) if i % 2 == 1 else x

def reverse_alternate4(st):
    return " ".join(rev(x, i) for i, x in enumerate(st.split()))

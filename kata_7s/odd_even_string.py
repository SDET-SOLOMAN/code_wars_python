# Given a string s, your task is to return another string such that even-indexed and odd-indexed
# characters of s are grouped and the groups are space-separated. Even-indexed group comes as first,
# followed by a space, and then by the odd-indexed part.
#
# Examples
#
# input:    "CodeWars" => "CdWr oeas"
#            ||||||||      |||| ||||
# indices:   01234567      0246 1357
# Even indices 0, 2, 4, 6, so we have "CdWr" as the first group.
# Odd indices are 1, 3, 5, 7, so the second group is "oeas".
# And the final string to return is "Cdwr oeas".
#
# Notes
#
# Tested strings are at least 8 characters long.


def sort_my_string(s):
    e = []
    o = []
    [e.append(x) if i % 2 else o.append(x) for i, x in enumerate(s)]

    return f"{''.join(o)} {''.join(e)}"


def sort_my_string2(s):
    return f'{s[::2]} {s[1::2]}'


def sort_my_string3(s):
    evs = ''
    ods = ''

    for num in range(len(s)):
        if s.index(s[num], num) % 2 == 0:
            evs += s[num]
        else:
            ods += s[num]

    return f"{evs} {ods}"
# Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.
#
# Examples
#
# As the article states, RLE is a very simple form of data compression. It's only suitable for runs of data, as one can see in the following example:
#
# run_length_encoding("hello world!")
#  //=>      [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
# It's very effective if the same data value occurs in many consecutive data elements:
#
# run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# # => [[34,'a'], [3,'b']]

def run_length_encoding(s):
    if not s:
        return []

    res = []
    temp = [0, s[0]]

    for i, char in enumerate(s):

        if char == temp[1]:
            temp[0] += 1
        else:
            res.append(temp)
            temp = [1, char]
        if i == len(s) - 1 and temp[1] != res[-1][1]:
            res.append(temp)

    return res

from itertools import groupby

def run_length_encoding2(s):
    return [[sum(1 for _ in g), k] for k, g in groupby(s)]
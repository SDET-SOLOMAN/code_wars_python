# Complete the solution so that it reverses all of the words within the string passed in.
#
# Words are separated by exactly one space and there are no leading or trailing spaces.
#
# Example(Input --> Output):
#
# "The greatest victory is that which requires no battle" --> "battle no requires which
# that is victory greatest The"

def reverse_words(s):
    s = s.split()
    return ' '.join(s[x] for x in range(-1, -len(s) - 1, -1))


def reverse_words2(s):
    return ' '.join(x for x in s.split()[::-1])


def reverseWords3(string):
    return ' '.join(reversed(string.split()))

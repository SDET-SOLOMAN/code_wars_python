# #
# Complete the solution so that it reverses all of the words within the string passed in.
#
# Words are separated by exactly one space and there are no leading or trailing spaces.
#
# Example(Input --> Output):
#
# "The greatest victory is that which requires no battle" -->
# "battle no requires which that is victory greatest The"

def reverse_words(s):
    return " ".join(s.split()[::-1])


def reverse_words2(s):
    s = s.split()

    return " ".join(s[x] for x in range(len(s) - 1, - 1, -1))
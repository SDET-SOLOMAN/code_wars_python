# Task
# If string has more than one neighboring dashes(e.g. --) replace they with one dash(-).
#
# Dashes are considered neighbors even if there is some whitespace between them.
#
# Example
# For str = "we-are- - - code----warriors.-"
#
# The result should be "we-are- code-warriors.-"
#
# Input/Output
# [input] string str
#
# [output] a string

def replace_dashes_as_one(s):
    a = s.replace('--','-').replace('- -', '-').replace('-  -', '-')
    if '--' in a or '- -' in a or '-  -' in a:
        return replace_dashes_as_one(a)
    return a

[9].ind
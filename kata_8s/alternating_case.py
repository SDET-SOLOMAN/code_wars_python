# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#
# Define String.prototype.toAlternatingCase (or a similar function/method such as
# to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for
# details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
#
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.

def to_alternating_case(string):
    return ''.join(x if not x.isalpha() else x.lower() if x.isupper() else x.upper() for x in string)


to_alternating_case2 = lambda string: ''.join(
    x if not x.isalpha() else x.lower() if x.isupper() else x.upper() for x in string)


up = lambda x: x.upper()
down = lambda x: x.lower()

def to_alternating_case3(string):
    return "".join([up(x), down(x)][x.isupper()] if x.isalpha() else x for x in string)


def to_alternating_case4(string):
    return string.swapcase()

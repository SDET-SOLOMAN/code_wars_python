# Given a string made of digits [0-9], return a string where each digit is
# repeated a number of times equals to its value.
#
# Examples
#
# explode("312")
# should return :
#
# "333122"
# explode("102269")
# should return :
#
# "12222666666999999999"

def explode(s):
    return ''.join([str(x) * int(x) for x in s])


def explode2(s):
    return ''.join(map(lambda x: str(x) * int(x), s))

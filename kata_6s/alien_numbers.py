# In a far far galaxy there is a population that write numbers using a strange system.
#
# They use the same digits ('0'–'9'), but in a different way.
#
# Task
# Try to decode their numbers.

def decode(number):
    x = ['0', '1', '00', '11', '000', '111', '0000', '1111', '00000', '11111']
    re = ''
    for n in number:
        re += x[int(n)]
    return int(re, 2)
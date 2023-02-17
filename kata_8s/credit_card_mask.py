# Usually when you buy something, you're asked whether your credit card number, phone number or answer
# to your most secret question is still correct. However, since someone could look over your shoulder,
# you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""
#
# // "What was the name of your first pet?"
#
# "Skippy" --> "##ippy"
#
# "Nananananananananananananananana Batman!"
# -->
# "####################################man!"

def maskify(cc):
    new_item = ""
    for char in cc[:-4]:
        new_item += '#'
    return new_item + cc[-4:]


def maskify2(cc):
    if len(cc) <= 4:
        return cc
    return ''.join('#' for x in cc[:-4]) + str(cc[-4:])


def maskify3(cc):
    c = len(cc)
    if c <= 4:
        return cc
    new_cc = ""
    for char in range(0, c - 4):
        new_cc += '#'
    return new_cc + cc[-4::1]
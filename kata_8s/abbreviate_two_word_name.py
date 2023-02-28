# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# patrick feeney => P.F

def abbrev_name(name):
    name = name.upper().split(" ")
    # return '.'.join(w[0] for w in name.split()).upper()
    # first, last = name.upper().split(' ')
    # return first[0] + '.' + last[0]
    return name[0][0] + "." + name[1][0]


def abbrev_name2(name):
    name = name.split()
    new_name = ''.join([x[0].upper() + "." for x in name])
    return new_name[:-1]


def abbrev_name3(name):
    name = name.upper().split()
    new_name = ''.join(x[0] + '.' for x in name)
    return new_name[:-1]


def abbrev_name4(name):
    return ''.join(x[0] + "." for x in name.upper().split())[:-1]

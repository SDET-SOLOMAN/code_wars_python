# DESCRIPTION:
# Note: This kata is inspired by Convert a Number to a String!. Try that one too.
#
# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?
#
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of
# an integral number.
#
# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

# just wanted to try something different
def string_to_number(s):
    d = {
        str(x): x for x in range(0, 10)
    }

    new = []
    minusik = False

    for char in s:
        if char.isdigit() and minusik == False:
            new.append(d[char])
        elif char == "-":
            print('here')
            minusik = True
        elif minusik and char.isdigit():
            print('sup')
            new.append(-d[char])
            minusik = False
    print(new)
    return int(''.join(str(x) for x in new))


def string_to_number2(s):
    return int(s)
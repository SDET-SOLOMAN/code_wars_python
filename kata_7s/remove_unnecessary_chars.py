# You've been given a list that states the daily revenue for each day of the week. Unfortunately, \
# the list has been corrupted and contains extraneous characters. Rather than fix the source of the problem,
# your boss has asked you to create a program that removes any unneccessary characters and return the corrected
# list.
#
# The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.
#
# For example:
#
# a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
# remove_char(a1)
# >>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']

def remove_char(a):
    result = []

    for item in a:
        digits = ""

        for char in item:
            if char.isdigit():
                digits += char

        if not digits:
            result.append('$0.00')
            continue

        if len(digits) == 1:
            dollars = '0'
            cents = '0' + digits
        elif len(digits) == 2:
            dollars = '0'
            cents = digits
        else:
            dollars = digits[:-2]
            cents = digits[-2:]
        clean = f"${dollars}.{cents}"

        result.append(clean)

    return result
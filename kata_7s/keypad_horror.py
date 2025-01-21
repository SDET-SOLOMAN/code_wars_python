# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# 7 8 9  \n
# 4 5 6  \n
# 1 2 3  \n
#   0 \n
#
# Cell phone keypad's layout:
# 1 2 3\n
# 4 5 6\n
# 7 8 9\n
#   0\n
#
# Solve the horror of unstandardized keypads by
# providing a function that converts computer input to a number as if it was typed on a phone.
#
# Example:
# "789" -> "123"
#
# Notes:
# You get a string with numbers only

def computer_to_phone(numbers):
    num = ''

    d = {
        '9': '3',
        '8': '2',
        '7': '1',
        '1': '7',
        '2': '8',
        '3': '9'
    }

    for char in numbers:
        if char == '0' or char == '4' or char == '5' or char == '6':
            num += char
        else:
            num += d.get(char)
    return num


def computer_to_phone2(numbers):
  return "".join([str({0:0, 1:7, 2:8, 3:9, 4:4, 5:5, 6:6, 7:1, 8:2, 9:3}[int(n)]) for n in numbers])


def computer_to_phone3(n):
    n = list(map(int, n))
    h, l = [7, 8, 9], [1, 2, 3]

    return "".join(map(str, [x - 6 if x in h else x + 6 if x in l else x for x in n]))
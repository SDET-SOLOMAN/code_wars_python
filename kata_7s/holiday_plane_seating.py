# Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again
# just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.
#
# To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters '
# I' and 'J' from their seat naming system.
#
# the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where
# the seat is (1-20 = front, 21-40 = middle, 41-60 = back). This number is followed by a letter,
# A-K with the exclusions mentioned above.
#
# Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.
#
# Given a seat number, your task is to return the seat location in the following format:
#
# '2B' would return 'Front-Left'.
#
# If the number is over 60, or the letter is not valid, return 'No Seat!!'.

def plane_seat(a):
    d = {
        "Position": {
            "Front": range(1, 21),
            "Middle": range(21, 41),
            "Back": range(41, 61),
        },
        "Direction": {
            "Left": "abc",
            "Middle": "def",
            "Right": "ghk",
        }
    }

    num = ""
    letter = ""

    for char in a:
        if char.isdigit():
            num += char
        else:
            letter += char.lower()

    if not num or not letter:
        return "No Seat!!"

    num = int(num)
    temp = ""

    for k, v in d["Position"].items():
        if num in v:
            temp += k + "-"

    if not temp:
        return "No Seat!!"

    for k, v in d["Direction"].items():
        if letter in v:
            return temp + k

    return "No Seat!!"

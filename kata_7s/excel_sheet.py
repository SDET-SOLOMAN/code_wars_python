# Write a function that, given a column title as it appears in an Excel sheet,
# returns its corresponding column number.
#
# All column titles will be uppercase.
#
# Examples:
#
# Column title: "A" --> return 1
# Column title: "Z" --> return 26
# Column title: "AA" --> return 27


def title_to_number(title):
    counting = 0
    for char in title:
        counting = counting*26 + ord(char) - 64
    return counting
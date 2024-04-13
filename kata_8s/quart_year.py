# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
#
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
# and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    my_dict = {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4
    }
    
    return my_dict[month]


def quarter_of2(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    return 4


def quarter_of3(month):
    d = {
        1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]
    }

    for k, v in d.items():
        if month in v:
            return k


def quarter_of4(month):
    match month:
        case 1 | 2 | 3:
            return 1
        case 4 | 5 | 6:
            return 2
        case 7 | 8 | 9:
            return 3
        case 10 | 11 | 12:
            return 4
# Your task is to get Zodiac Sign using input day and month.
#
# For example:
#
# get_zodiac_sign(1,5) => 'Taurus'
# get_zodiac_sign(10,10) => 'Libra'
# Correct answers are (preloaded):
#
# SIGNS = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer',
# 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
# P.S. Each argument is correct integer number.
#
# WESTERN ASTROLOGY STAR SIGN DATES
#
# Aries (March 21-April 19)
# Taurus (April 20-May 20)
# Gemini (May 21-June 20)
# Cancer (June 21-July 22)
# Leo (July 23-August 22)
# Virgo (August 23-September 22)
# Libra (September 23-October 22)
# Scorpio (October 23-November 21)
# Sagittarius (November 22-December 21)
# Capricorn (December 22-January 19)
# Aquarius (January 20 to February 18)
# Pisces (February 19 to March 20)


def get_zodiac_sign(d, m):
    zodiac_signs = {
        "Aries": {"month": [3, 4], "day": [21, 19]},
        "Taurus": {"month": [4, 5], "day": [20, 20]},
        "Gemini": {"month": [5, 6], "day": [21, 20]},
        "Cancer": {"month": [6, 7], "day": [21, 22]},
        "Leo": {"month": [7, 8], "day": [23, 22]},
        "Virgo": {"month": [8, 9], "day": [23, 22]},
        "Libra": {"month": [9, 10], "day": [23, 22]},
        "Scorpio": {"month": [10, 11], "day": [23, 21]},
        "Sagittarius": {"month": [11, 12], "day": [22, 21]},
        "Capricorn": {"month": [12, 1], "day": [22, 19]},
        "Aquarius": {"month": [1, 2], "day": [20, 18]},
        "Pisces": {"month": [2, 3], "day": [19, 20]}
    }

    for sign, data in zodiac_signs.items():

        start_month, end_month = data["month"]
        start_day, end_day = data["day"]

        if m == start_month and d >= start_day:
            return sign
        elif m == end_month and d <= end_day:
            return sign

    return "Unknown"

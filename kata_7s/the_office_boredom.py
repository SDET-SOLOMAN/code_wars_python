# Each department has a different boredom assessment score, as follows:
#
# accounts = 1
# finance = 2
# canteen = 10
# regulation = 3
# trading = 6
# change = 6
# IS = 8
# retail = 5
# cleaning = 4
# pissing about = 25
#
# Depending on the cumulative score of the team, return the appropriate sentiment:
#
# <=80: 'kill me now'
# < 100 & > 80: 'i can handle this'
# 100 or over: 'party time!!'

def boredom(staff):
    departments = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25
    }

    s = sum(departments.get(v, 0) for k, v in staff.items())

    return "party time!!" if s >= 100 else 'i can handle this' if s > 80 else "kill me now"
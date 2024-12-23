# Introduction
#
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side
# letters was too high and the war began.
#
# Task
#
# Write a function that accepts fight string consists of only small letters and return who wins the fight.
# When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other
# case return Let's fight again!.
#
# The left side letters and their power:
#
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#
#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
#
# Example
#
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!

def alphabet_war(fight):
    re = "Let's fight again!"
    s = 0
    fight = fight.lower()

    right = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }

    left = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }

    for char in fight:
        if char in right:
            s -= right[char]
        elif char in left:
            s += left[char]

    return re if s == 0 else "Right side wins!" if s < 0 else "Left side wins!"


def alphabet_war2(fight):
    re = "Let's fight again!"
    left = "Left "
    right = "Right "
    text = "side wins!"
    fight = fight.lower()

    d = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
        'm': -4,
        'q': -3,
        'd': -2,
        'z': -1
    }

    s = sum(d[c] for c in fight if c in d)

    return re if s == 0 else [left, right][s < 0] + text

# You are the rock paper scissors oracle.
#
# Famed throughout the land, you have the incredible ability to predict which hand gestures your opponent will choose
# out of rock, paper and scissors.
#
# Unfortunately you're no longer a youngster, and have trouble moving your hands between rounds. For this reason,
# you can only pick a single gesture for each opponent. If it's possible for you to win, you will, but you're also happy to tie.
#
# Given an array of gestures — for example ["paper", "scissors", "scissors"] — return the winning gesture/s
# in the order in which they appear in the title, separated by a forward slash. For example, if rock and scissors
# could both be used to win you would return:
#
# "rock/scissors"
#
# If it's not possible for you to win then return:
#
# "tie"

combo = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}


def checker(me, them):
    if me == them:
        return 0
    return 1 if combo[me] == them else -1


total_score = lambda my, ges: sum(checker(my, g) for g in ges)


def oracle(ges):
    res = [my for my in combo if total_score(my, ges) > 0]
    if len(res) > 1:
        res.sort(key=lambda x: not combo[x])
    return '/'.join(res) if res else 'tie'
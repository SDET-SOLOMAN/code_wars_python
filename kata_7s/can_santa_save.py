# Can Santa save Christmas?
#
# Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
#
# But he has only 24 hours left. Can he do it?
#
# Your Task:
#
# You will get an array as input with time durations as string in the following format: HH:MM:SS.
# Each duration represents the time taken by Santa to deliver a present. Determine whether
# he can do it in 24 hours or not. In case the time required to deliver all of the presents
# is exactly 24 hours, Santa can complete the delivery ;-) .


def determine_time(arr):
    if not arr:
        return True

    h, m, s = 0, 0, 0

    for char in arr:
        x, x1, x2 = [int(s) for s in char.split(":")]
        h += x
        m += x1
        s += x2
        
    m //= 60
    s //= 60
    return (h + m + s) <= 24
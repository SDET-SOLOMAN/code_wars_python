# This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.
#
# Task:
#
# Find out "B"(Bug) in a lot of "A"(Apple).
#
# There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.
#
# input: string Array apple
#
# output: Location of "B", [x,y]


def sc(apple):
    index_1 = 0
    index_2 = 0
    for char in apple:
        for ch in char:
            if ch == "B":
                return [index_1, index_2]
            index_2 += 1
        index_1 += 1
        index_2 = 0
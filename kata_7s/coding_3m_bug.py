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


def sc2(apple):
    for index_1, row_1 in enumerate(apple):
        for index_2, row_2 in enumerate(row_1):
            if row_2.lower() == 'b':
                return [index_1, index_2]


sc3 = lambda apple: [[index1, char1.index("B")] for index1, char1 in enumerate(apple) if "B" in char1][0]
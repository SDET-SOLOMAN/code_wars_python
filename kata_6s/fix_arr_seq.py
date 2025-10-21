# Assume we take a number x and perform any one of the following operations:
#
# a) Divide x by 3 (if it is divisible by 3), or
# b) Multiply x by 2
# After each operation, we write down the result. If we start with 9, we can get a sequence such as:
#
# [9,3,6,12,4,8] -- 9/3=3 -> 3*2=6 -> 6*2=12 -> 12/3=4 -> 4*2=8
# You will be given a shuffled sequence of integers and your task is to reorder them so that they conform to the above sequence. There will always be an answer.
#
# For the above example:
# solve([12,3,9,4,6,8]) = [9,3,6,12,4,8].

def solve(arr):
    a = set(arr)

    start = None

    for x in a:
        if (x * 3) not in a and (x % 2 != 0 or (x // 2) not in a):
            start = x
            break

    re = [start]

    while len(re) < len(arr):
        x = re[-1]
        if x % 3 == 0 and (x // 3) in a:
            re.append(x // 3)
        else:
            re.append(x * 2)
    return re

# someone's solution on codewars
def solve2(arr):

    for num in arr:
        temp = [num]

        while True:
            print(temp)
            t = temp[-1]

            if t % 3 == 0 and t // 3 in arr:
                temp.append(t // 3)
            elif t * 2 in arr:
                temp.append(t * 2)
            else:
                break
            print(temp)

        if len(temp) == len(arr):
            return temp
    return None

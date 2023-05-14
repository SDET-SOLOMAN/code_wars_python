# Task
#
# You will be given an array of numbers. You have to sort the odd numbers in
# ascending order while leaving the even numbers at their original positions.
#
# Examples
#
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    a = sorted([x for x in source_array if x % 2 != 0])
    new_s = []
    index = 0
    for num in source_array:
        if num in a:
            new_s.append(a[index])
            index += 1
        else:
            new_s.append(num)
    return new_s


def sort_array2(source_array):
    odds = []
    answer = []

    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")

        else:
            answer.append(i)

    odds.sort()

    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer


def sort_array3(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])
    ind = 0
    answer = []

    for index, num in enumerate(source_array):

        if num % 2 == 0:
            answer.append(num)
        else:
            answer.append(odds[ind])
            ind += 1

    return answer


def sort_array4(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]

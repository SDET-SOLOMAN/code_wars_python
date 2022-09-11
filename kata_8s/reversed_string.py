# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def solution(string):
    return string[::-1]


def solution2(string):
    new_string = ""
    index = -1 * (len(string) - 1)
    for char in string:
        print(string[index])
        index += 1
    return new_string
print(solution2("world"))
# Task:
# You are given a word target and list of sorted(by length(increasing), number of upper case letters(decreasing),
# natural order) unique words words which always contains target, your task is to find the index(0 based)
# of target in words,which would always be in the list.
#
# Examples:
# words = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars']
# '''
# (list is sorted by length(small to big), then by number of uppercase letters(maximum to minimum)
# and then by natural order)
# '''
# target = 'codewars'
# #result should be 7
#
# #Another example:
# words = ['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj']
# target = 'akC'
# #result should be 9
# Constraints:
# python
# 4 < len(words) <= 200000
# 1 < len(search) <= 10
# Number of random tests are around 6000.
# Reference solution passes in 8s.
# Javascript
# Your solution must pass in less than ref.solution+10ms speed.
# This is because generating long list of unique words in js is slow.
# If you think you've got an correct approach and timing test is not passing then submit again.

# solved it using binary search
def index_of(words, target):
    left, right = 0, len(words) - 1
    target_len = len(target)
    target_upper = sum(1 for c in target if c.isupper())

    while left <= right:
        mid = (left + right) // 2
        mid_word = words[mid]
        mid_len = len(mid_word)
        mid_upper = sum(1 for c in mid_word if c.isupper())

        if mid_len < target_len:
            left = mid + 1
        elif mid_len > target_len:
            right = mid - 1
        else:
            if mid_upper > target_upper:
                left = mid + 1
            elif mid_upper < target_upper:
                right = mid - 1
            else:
                if mid_word < target:
                    left = mid + 1
                elif mid_word > target:
                    right = mid - 1
                else:
                    return mid

    return -1
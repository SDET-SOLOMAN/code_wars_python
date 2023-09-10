# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same
# l return the first in order of appearance.

# For empty string return:

# ('', 0)
# Happy coding! :)
def longest_repetition(chars):
    my_char = ''
    my_count = 0
    for num in range(len(chars)):
        calc = 0
        temp_char = chars[num]
        while chars[num] == temp_char:
            calc += 1
            if num < len(chars) - 1:
                num += 1
            else:
                break
        if calc > my_count:
            my_count = calc
            my_char = temp_char
    return (my_char, my_count)


def longest_repetition2(chars):
    last = ''
    count = 0
    return_st = (last, count)

    for c in chars:
        if c == last:
            count += 1
        else:
            last = c
            count = 1
        if return_st[1] < count:
            return_st = (last, count)
    return return_st
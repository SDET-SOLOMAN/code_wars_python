# This time no story, no theory. The examples below show you how to write function accum:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    count = 1
    new_string = ""
    for letter in s:
        new_string += (letter * count).capitalize()
        new_string += "-"
        count += 1
    return new_string[:-1]


def accum2(s):
    new_text = ""
    for num in range(0, len(s)):
        new_text += s[num].upper() + s[num].lower() * num + "-"
    return new_text[:-1]

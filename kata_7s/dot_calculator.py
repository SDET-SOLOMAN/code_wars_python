# Dot Calculator
#
# You have to write a calculator that receives strings for input.
# The dots will represent the number in the equation. There will be dots on one side, an operator,
# and dots again after the operator. The dots and the operator will be separated by one space.
#
# Here are the following valid operators :
#
# + Addition
# - Subtraction
# * Multiplication
# // Integer Division
# Your Work (Task)
#
# You'll have to return a string that contains dots, as many the equation returns.
# If the result is 0, return the empty string. When it comes to subtraction,
# the first number will always be greater than or equal to the second number.
#
# Examples (Input => Output)
#
# * "..... + ..............." => "...................."
# * "..... - ..."             => ".."
# * "..... - ."               => "...."
# * "..... * ..."             => "..............."
# * "..... * .."              => ".........."
# * "..... // .."             => ".."
# * "..... // ."              => "....."
# * ". // .."                 => ""
# * ".. - .."                 => ""

def calculator(txt):
    left = 0
    switch = False
    right = 0
    operator = ""

    for char in txt:

        if char == " ":
            switch = True

        if not switch and char == ".":
            left += 1

        elif switch and char == ".":
            right += 1

        if char in "-+/*":
            operator = char
            if operator == "/":
                operator = "//"

    return {

        '+': left + right,
        '-': left - right,
        '//': left // right,
        '*': left * right

    }[operator] * "."


def calculator2(txt):
    txt = txt.split(" ")
    print(txt)
    val1 = sum(1 for x in txt[0])
    val2 = sum(1 for x in txt[2])

    dict_ = {

        '+': val1 + val2,
        '-': val1 - val2,
        '//': val1 // val2,
        '*': val1 * val2

    }

    return dict_[txt[1]] * "."
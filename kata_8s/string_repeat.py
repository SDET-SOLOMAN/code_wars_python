# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# Examples (input -> output)

# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat

def repeat_str2(repeat, string):
    index = 0
    new_string = ''
    while index < repeat:
        new_string += string
        index += 1
    return new_string
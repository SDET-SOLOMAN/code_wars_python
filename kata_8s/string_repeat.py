# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# Examples (input -> output)

# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat

def repeat_str2(repeat, string):
    counter = 0
    new_string = ''
    while counter < repeat:
        new_string += string
        counter += 1
    return new_string

def repeat_str3(repeat, string):
    new_word = ''
    for num in range(0, repeat):
        new_word += string
    return new_word
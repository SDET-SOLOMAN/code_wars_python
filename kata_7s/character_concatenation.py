# Given a string, you progressively need to concatenate the first character from the left and the first character from the right and "1", then the second character from the left and the second character from the right and "2", and so on.

# If the string's length is odd drop the central element.

# For example:

# "abcdef"  --> "af1be2cd3"
# "abc!def" --> "af1be2cd3" // same result

def char_concat(word):
    
    f = word[:len(word) // 2]
    s = word[len(word) // 2:][::-1]
    
    return "".join(f[x] + s[x] + str(x + 1) for x in range(len(f)))


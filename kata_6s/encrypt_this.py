# Acknowledgments:
# I thank yvonne-liu for the idea and for the example tests :)
#
# Description:
# Encrypt this!
#
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
#
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

encrypt_this = lambda text: ' '.join(str(ord(x[0])) + x[-1]  + x[2:-1] + x[1]
                                     if len(x) >= 3 else str(ord(x[0])) + x[1:] for x in text.split()) if text else ""

# using a for loop
def encrypt_this2(text):
    new_s = []
    text = text.split()
    for char in text:
        tempo = ''
        if len(char) >= 3:
            tempo += str(ord(char[0])) + char[-1] + char[2:-1] + char[1]
        else:
            if len(char) == 2:
                tempo += str(ord(char[0])) + char[1:]
            elif len(char) == 1:
                tempo += str(ord(char[0]))
        new_s.append(tempo)
    return ' '.join(new_s)

# found these solutions in some other's solutions, looks good, so added here
def process_word(word):
    return str(ord(word[0])) + ((word[-1] + word[2:-1] + word[1]) if len(word) > 2 else word[1:])

def encrypt_this3(text):
    return " ".join(map(process_word, text.split()))


def encrypt_this4(text):
    result = []
    for i in text.split():
        i = list(i)
        if len(i) > 2:
            i[-1], i[1] = i[1], i[-1]
        i[0] = str(ord(i[0]))
        result.append("".join(i))
    return " ".join(result)
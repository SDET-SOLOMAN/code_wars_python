# Description
# In English we often use "neutral vowel sounds" such as "umm", "err", "ahh" as
# fillers in conversations to help them run smoothly.
#
# Bob always finds himself saying "err". Infact he adds an "err" to every single
# word he says that ends in a consonant! Because Bob is odd, he likes to stick to
# this habit even when emailing.
#
# Task
# Bob is begging you to write a function that adds "err" to the end of every word
# whose last letter is a consonant (not a vowel, y counts as a consonant).
#
# The input is a string that can contain upper and lowercase characters, some
# punctuation but no numbers. The solution should be returned as a string.
#
# NOTE: If the word ends with an uppercase consonant, the following "err" will be uppercase --> "ERR".
#
# eg:
#
# "Hello, I am Mr Bob" --> "Hello, I amerr Mrerr Boberr"
#
# "THIS IS CRAZY!"  --> "THISERR ISERR CRAZYERR!"

def err_bob(st):
    x = "auioe"

    d = {
        True: "ERR",
        False: "err"
    }

    w = ""
    temp = ""

    for i, char in enumerate(st):
        if char.isalpha():
            temp += char
        else:
            if temp and temp[-1].lower() not in x:
                temp += d[temp[-1].isupper()]
            w += temp + char
            temp = ""

    return w if not temp else w + temp if temp[-1].lower() in x else w + temp + d[temp[-1].isupper()]
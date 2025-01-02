# Unscramble the eggs.
#
# The string given to your function has had an "egg" inserted directly after each consonant.
# You need to return the string before it became eggcoded.
#
# Example
# unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
# //             "B---eg---in---n---er---"
# Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.

def unscramble_eggs(word):
    word = word.replace("egg", "---")
    return ''.join(x for x in word if x != "-")


def unscramble_eggs2(word):
    new_word = ""
    num = 0
    for i, n in enumerate(word):

        if i - 2 < num:
            if word[num: num + 3] != 'egg':
                new_word += word[num]
                num += 1
        else:
            num += 3

    return new_word


def unscramble_eggs3(word):
    return ''.join(word.replace("egg", ""))


def unscramble_eggs(word):
    e = "egg"
    i = 0
    new = ""

    for num in range(len(word)):
        try:
            if word[i:i + 3] != e:
                new += word[i]
                i += 1
            else:
                i += 3
        except:
            pass

    return new
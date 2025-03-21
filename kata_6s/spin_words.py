# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata). Strings
# passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    return ' '.join([x[::-1] if len(x) >= 5 else x for x in sentence.split()])


######################################
rev = lambda x: x[::-1] if len(x) >= 5 else x


def spin_words2(sentence):
    return ' '.join(rev(x) for x in sentence.split())


######################################

def rev2(word):
    new_word = ''
    l = len(word)
    if l >= 5:
        for char in range(l - 1, -1, -1):
            new_word += word[char]
        return new_word
    return word


def spin_words3(sentence):
    return ' '.join(rev2(x) for x in sentence.split())


spin_words4 = lambda sentence: ' '.join(map(lambda x: rev2(x), sentence.split()))

# -------------------

len_check = lambda x: len(x) >= 5


def rev(x):
    s = ""

    for char in range(-1, -len(x) - 1, - 1):
        s += x[char]

    return s


def spin_words4(sentence):
    return " ".join(rev(x) if len_check(x) else x for x in sentence.split())


is_it = lambda x: len(x) > 4
rev2 = lambda x: x[::-1]


def spin_words5(sentence):
    # Your code goes here
    return " ".join(rev2(x) if is_it(x) else x for x in sentence.split())

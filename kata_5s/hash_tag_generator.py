# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
#
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    if not s or len(s) > 139:
        return False
    return "#" + ''.join(x[0].upper() + x[1:].lower() for x in s.split())


generate_hashtag2 = lambda word: "#" + ''.join(x.title() for x in word.split()) if word and len(word) < 140 else False

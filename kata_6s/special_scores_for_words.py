# We define a special score for a word (ssw) as follows. We multiply the corresponding ASCII decimal code
# for each letter of the word by its respective frequency of this letter in the word, collect
# these addens and sum them up.
#
# For example, for the word investigation, we have the respective ASCII codes and frequencies for each letter:
#
# Letter    ASCII decimal code        Letter Frequency (in "investigation")
#  i             105                            3
#  n             110                            2
#  t             116                            2
#  a              97                            1
#  e             101                            1
#  g             103                            1
#  o             111                            1
#  s             115                            1
#  v             118                            1
# So the ssw for this word will be:
#
# ssw = 105 * 3 + 110 * 2 + 116 * 2 + 97 * 1 + 101 * 1 + 103 * 1 + 111 * 1 + 115 * 1 + 118 * 1 = 1412
# Task
# Complete the function that receives two arguments,
#
# number of letters, num_let
# maximum special score max_ssw for the word
# You were also provided with a list of 2000 words of the Oxford Dictionary Of English (U.K. English),
# named WORD_LIST for python, $word_list for ruby, wordList for JavaScript.
#
# The function should output a word from the database of 2000 words that has the highest possible ssw
# of the given number of letters but smaller or equal to the given max_ssw.
#
# If we have more than one word with the same number of letters, num_let, and the same special score, ssw,
# choose the largest word in lexicographical order.
#
# If there are no words in the database that satisfies the given num_let and max_ssw, return None in Python,
# nil in Ruby, null in JavaScript.
#
# Example
# Let's see some cases:
#
# num_let = 8
# max_ssw = 888
# # There are three words with 8 letters and with ssw == 888
# #   "question", "security" and "southern"
# # The list of these words sorted with its respective ssw is
# #   [(888, "question"), (888, "security"), (888, "southern")],
# # "southern" should be chosen
#
# num_let = 9
# max_ssw = 500
# # The word of 9 letters with minimum ssw is "candidate" with ssw = 925
# # There are no 9 letter words with less than or equal to 500 ssw
# # Should return None in Python, nil in Ruby, null in JavaScript


def multi(word):
    # Use set(word) to avoid counting the same letter multiple times
    return sum(ord(char) * word.count(char) for char in set(word))

def find_word(num_let, max_ssw):
    possible_words = [word for word in ["WORD_LIST"] if len(word) == num_let]
    score_dict = {word: multi(word) for word in possible_words}
    valid_words = {word: score for word, score in score_dict.items() if score <= max_ssw}

    if not valid_words:
        return None

    max_score = max(valid_words.values())

    best_words = [word for word, score in valid_words.items() if score == max_score]
    return max(best_words)

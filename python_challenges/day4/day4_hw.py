# Enter a string of words separated by spaces. Find the longest word.

my_word = 'Khachapuri is the traditional Georgian Dish'


# 1st way

def long_string_word(word: str):
    word1 = ''
    word2 = ''
    index = 0
    for char in word:
        if char == " ":
            if len(word1) > len(word2):
                word2 = word1
            word1 = ''
        elif char != " ":
            word1 += char
    return len(word2)


# 2nd way

def long_string_word2(word='Khachapuri is the traditional Georgian Dish'):
    my_words = word.split(" ")
    counting_chars = sorted([len(x) for x in my_words], reverse=True)
    return counting_chars[0]


print(long_string_word2())
print(long_string_word(my_word))


# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string, and
# words may be separated by several spaces). Make the string regular (delete all spaces at the beginning and end of
# the string, leave one space separating words).

# 1st way

def irreg_string_converter(word='         Khachapuri       is       the        traditional    Georgian     Dish'):
    return ' '.join(word.split())


# 2nd way

def irreg_string_converter2(word='        Khachapuri       is       the        traditional    Georgian     Dish '
                                 '        '):
    my_new_string = ''
    index = 0
    for char in word:
        if char != " ":
            my_new_string += char
        elif char == " " and word[index - 1] != " ":
            my_new_string += " "
        index += 1
    if my_new_string[0] == " ":
        return my_new_string[1:]
    return my_new_string


print(irreg_string_converter2())
print(irreg_string_converter())


# Write a Python function, which will count how many times
# a character (substring) is included in a string. DON’T USE METHOD COUNT

def char_count(word: str, char: str):
    char_counter = 0
    index = word.find(char)
    while index > - 1:
        print(index)
        index = word.find(char, index + 1)
        char_counter += 1
    return char_counter


print(char_count('Khachapuri is eo the traditional Georgian Dish', 'eo'))



# replace one substring with another

def let_replace(word, char_old, char_new):
    len_old_char = len(char_old)
    index = word.find(char_old)
    return word[:index] + char_new + word[index:]

print("dcdcidcidcvidjvidjvfijdvdivj".replace('ci', 'ha'))
print(let_replace('dcdcidcidcvidjvidjvfijdvdivj', 'ci', 'ha'))

# # 1st way ISOGRAM
#
# def is_isogram(word='Hello'):
#     new_str = ""
#     for char in word:
#         if char not in new_str:
#             new_str += char
#         else:
#             return False
#     return True
#
#
# # 2nd way isogram
#
# def is_isogram2(word='Hello'):
#     m = ''.join(set(word))
#     return len(word) == len(m)
#
#
# print(is_isogram2('hello'))
# print(is_isogram('helo'))
#
#
# # string compression a4b3c2e
# # 1st way
# def string_compr(word='aaaabbbbcccccccee'):
#     my_string = ''
#     for char in word:
#         if char not in my_string:
#             my_string += char
#             my_string += str(word.count(char))
#     return my_string
#
#
# def string_compr2(word='aaaabbbbcccccccee'):
#     index = 0
#     counter = 0
#     new_str = ''
#     for char in word:
#         if char not in new_str:
#             new_str += char
#             while counter < len(word):
#                 if word[counter] == char:
#                     index += 1
#                 counter += 1
#             if index > 1:
#                 new_str += str(index)
#             index = 0
#             counter = 0
#     return new_str
#
#
# print(string_compr2("ncrncrncjncsjcnncjskdcnskdjcndskncsdkjncsjcnjcbndhcvbfhbv"))
# print(string_compr("ncrncrncjncsjcnncjskdcnskdjcndskncsdkjncsjcnjcbndhcvbfhbv"))
#
#
# # decompress string
#
# def string_decompr(word='a5b3h3c19n2ww'):
#     new_string = ''
#     count = ''
#     for char in word[::-1]:
#         if char.isalpha():
#             if len(count) > 0:
#                 new_string += char * int(count[::-1])
#             else:
#                 new_string += char
#             count = ""
#         if char.isdigit():
#             count += char
#     return new_string[::-1]
#
#
# print(string_decompr())

# reverse a string

def lets_reverse(word: str):
    # opt 1:
    # word[::-1]

    # opt 2:
    # ''.join(reversed(word))

    # opt 3:
    new_word = ""
    index = len(word) - 1
    while index >= 0:
        new_word += word[index]
        index -= 1
    return new_word


print(lets_reverse('JAMEsss Mike'))


# divide string to half

def split_half(word: str):
    string_len = len(word) // 2
    print(string_len)
    return word[:string_len + 1]


print(split_half('jamesssss'))


# delete a fragment between two query chars

def delete_frag(word: str, removing_by='h'):
    new_str = ''
    skipping = False
    for char in word:
        if char == removing_by:
            if not skipping:
                skipping = True
            elif skipping:
                skipping = False
        elif not skipping:
            new_str += char
    return new_str


def del_frag2(string, char):
    first = string.find(char)
    second = string.rfind(char)
    return string[:first] + string[second + 1:]


print(delete_frag('myhacgsshpuri', "h"))
print(del_frag2('myhacgsshpuri', "h"))


# unique chars in string

def del_unqiue(word):
    new_word = ''
    for char in word:
        if char not in new_word:
            new_word += char
    return new_word


print(del_unqiue('vnfjvnfjvndjkvnfdvkndfvkndfjnkvfdnkj'))
print(''.join(list(set("vnfjvnfjvndjkvnfdvkndfvkndfjnkvfdnkj"))))
# Count the number of Duplicates
#
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets (both
# uppercase and lowercase) and numeric digits.
#
# Example
#
# "abcde" -> 0  # no characters repeats more than once
# "aabbcde" -> 2  # 'a' and 'b'
# "aabBcde" -> 2  # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1  # 'i' occurs six times
# "Indivisibilities" -> 2  # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2  # 'a' and '1'
# "ABBA" -> 2  # 'A' and 'B' each occur twice

def duplicate_count(text):
    return len(list(set([x for x in text.lower() if text.lower().count(x) > 1])))


def duplicate_count2(text):
    lett = [x for x in text.lower()]
    nuu = []
    for num in lett:
        if lett.count(num) > 1:
            if num not in nuu:
                nuu.append(str(num))
    return len(nuu)


def duplicate_count3(text):
    my_dict = {

    }

    text = text.lower()

    for char in text:
        if my_dict.get(char):
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    my_count = 0

    for k, v in my_dict.items():
        if v > 1:
            my_count += 1

    return my_count


def duplicate_count4(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)
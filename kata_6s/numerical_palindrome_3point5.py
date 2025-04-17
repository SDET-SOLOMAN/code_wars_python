# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 2332, 110011, 54322345
#
# For a given number num, write a function which returns an array of all the numerical palindromes contained within each number. The array should be sorted in ascending order and any duplicates should be removed.
#
# In this kata, single digit numbers and numbers which start or end with zeros (such as 010 and 00) are NOT considered valid numerical palindromes.
#
# If num contains no valid palindromes, return "No palindromes found". Otherwise, return "Not valid" if the input is not an integer or is less than 0.
#
# Examples
#
# 1221      -->  [22, 1221]
# 34322122  -->  [22, 212, 343, 22122]
# 1001331   -->  [33, 1001, 1331]
# 1294      -->  "No palindromes found"
# "1221"    -->  "Not valid"

def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"

    num_str = str(num)
    found = set()

    for i in range(len(num_str)):
        for j in range(i + 1, len(num_str)):
            substr = num_str[i:j + 1]
            if substr == substr[::-1] and len(substr) > 1:
                if not (substr.startswith('0') or substr.endswith('0')):
                    found.add(int(substr))

    return sorted(found) if found else "No palindromes found"
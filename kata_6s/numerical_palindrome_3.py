# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.
# Examples of numerical palindromes are:
#
# 2332
# 110011
# 54322345
#
# For a given number num, write a function which returns the number of numerical palindromes within each number.
# For this kata, single digit numbers will NOT be considered numerical palindromes.
#
# Return "Not valid" if the input is not an integer or is less than 0.
#
# palindrome(5) => 0
# palindrome(1221) => 2
# palindrome(141221001) => 5
# palindrome(1294) => 0
# palindrome("1221") => "Not valid"

def palindrome(num):
    if type(num) != int or num < 0:
        return "Not valid"

    re = 0
    n = str(num)

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i : j + 1] == n[i : j + 1][::-1]:
                re += 1
    return re
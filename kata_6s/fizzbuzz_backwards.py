# Traditionally in FizzBuzz, multiples of 3 are replaced by "Fizz" and multiples of 5 are replaced by "Buzz".
# But we could also play FizzBuzz with any other integer pair [n, m] whose multiples are replaced with Fizz and Buzz.
#
# For a sequence of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers whose multiples are being replaced
# by Fizz and Buzz. Return them as an array [n, m]
#
# The Fizz and Buzz numbers will always be integers between 1 and 50, and the sequence will have a maximum
# length of 100. The Fizz and Buzz numbers might be equal, and might be equal to 1.
#
# Examples
# Classic FizzBuzz; multiples of 3 are replaced by Fizz, multiples of 5 are replaced by Buzz:
# [1, 2, "Fizz", 4, "Buzz", 6]  ==>  [3, 5]
# Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz:
# [1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]  ==>  [2, 3]
# Multiples of 2 are replaced by Fizz and Buzz:
# [1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]  ==>  [2, 2]
# Fizz = 1, Buzz = 6:
# ["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]  ==>  [1, 6]

def reverse_fizz_buzz(array):

    fizz_num = None
    buzz_num = None

    for indexx, num in enumerate(array, 1):
        if type(num) == str:
            is_fizz = "Fizz" in num
            is_buzz = "Buzz" in num
            if is_fizz and not fizz_num:
                fizz_num = indexx
            if is_buzz and not buzz_num:
                buzz_num = indexx

    if fizz_num and not buzz_num:
        buzz_num = fizz_num
    if buzz_num and not fizz_num:
        fizz_num = buzz_num

    return (fizz_num, buzz_num)


def reverse_fizz_buzz2(array):
    fizz = array.index("Fizz") if "Fizz" in array else array.index("FizzBuzz")
    buzz = array.index("Buzz") if "Buzz" in array else array.index("FizzBuzz")
    return (fizz+1, buzz+1)

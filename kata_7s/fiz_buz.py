# Return an array containing the numbers from 1 to N, where N is the parametered value.
#
# Replace certain values however if any of the following conditions are met:
#
# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.
#
# Method calling example:
#
# fizzbuzz(3) -->  [1, 2, "Fizz"]

def secret_formula(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return n


fizzbuzz_simple = lambda numbers: list(map(secret_formula, range(1, numbers + 1)))


def fizzbuzz(n):
    return list(map(lambda x: "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else
    "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x, range(1, n + 1)))


def fizzbuzz2(n):
    new_n = []
    for char in range(1, n + 1):
        if char % 3 == 0 and char % 5 == 0:
            new_n.append('FizzBuzz')
        elif char % 3 == 0:
            new_n.append('Fizz')
        elif char % 5 == 0:
            new_n.append('Buzz')
        else:
            new_n.append(char)
    return new_n

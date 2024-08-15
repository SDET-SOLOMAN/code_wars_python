# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

simple_multiplication = lambda x: [x * 8, x * 9][x % 2]


def simple_multiplicatio2(number) :
    return number * 9 if number % 2 else number * 8
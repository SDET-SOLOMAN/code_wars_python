# Summation Of Primes
#
# The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below or equal to the number passed in.


def summation_of_primes(primes):
    t = 0

    for num in range(2, primes + 1):  # start from 2 since 0 and 1 are not prime
        temp = True
        for n in range(2, int(num**0.5) + 1):  # more efficient check
            if num % n == 0:
                temp = False
                break  # no need to keep checking if already divisible
        if temp:
            t += num
    return t


checker = lambda x: all(x % n != 0 for n in range(2, int(x ** 0.5) + 1)) if x > 1 else False

def summation_of_primes2(primes):
    return sum(num for num in range(2, primes + 1) if checker(num))


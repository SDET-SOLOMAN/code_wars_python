# Not considering number 1, the integer 153 is the first integer having this property: the sum of the third-power
# of each of its digits is equal to 153. Take a look: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
#
# The next number that experiments this particular behaviour is 370 with the same power.
#
# Write the function eq_sum_powdig(), that finds the numbers below a given upper limit hMax (inclusive)
# that fulfills this property but with different exponents as the power for the digits.
#
# eq_sum_powdig(hMax, exp): ----> sequence of numbers (sorted list) (Number one should not be considered).
#
# Let's see some cases:
#
# eq_sum_powdig(100, 2) ----> []
#
# eq_sum_powdig(1000, 2) ----> []
#
# eq_sum_powdig(200, 3) ----> [153]
#
# eq_sum_powdig(370, 3) ----> [153, 370]

def is_valid(number, exp):
    n = number
    temp = 0

    while n > 0:
        temp += (n % 10) ** exp
        n //= 10
    return temp == number
    # sum_of_powers = sum(int(digit) ** exp for digit in str(number))
    # return sum_of_powers == number

def eq_sum_powdig(h_max, exp):
    return [x for x in range(10, h_max + 1) if is_valid(x, exp)]
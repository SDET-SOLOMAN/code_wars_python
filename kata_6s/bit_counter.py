# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
# representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def count_bits(char):
    my_bin = ''
    while char > 0:
        my_bin += str(char % 2)
        char //= 2
    counter = 0
    for ch in my_bin:
        if ch == '1':
            counter += 1
    return counter


def countBits2(n):
    return bin(n).count("1")
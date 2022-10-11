# Find the max bin gap between 0s for a given num

# 529 = 10000110001. The bin gap is equal to 4

# ONE WAY
# my_num = bin(529)

# we can use def func insted of bin method

# SECOND WAY

def to_bin_converter(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]


my_zero_count = 0
my_other_count = 0

my_num = to_bin_converter(529)
print(my_num)

for num in my_num[2:]:
    if int(num) == 0:
        my_other_count += 1
    else:
        if my_zero_count < my_other_count:
            my_zero_count = my_other_count
        my_other_count = 0
print(my_zero_count)

# fibonacci

num = 10


def my_fib(numba=4):
    if numba == 0:
        return [0]
    elif numba == 1 or numba == 2:
        return [0, 1, 1]
    elif not isinstance(numba, int):
        return ValueError
    else:
        my_num = [0, 1, 1]
        num1 = 1
        num2 = 1
        n = 3
        while n < numba:
            my_num.append(num1 + num2)
            num1, num2 = num2, num1 + num2
            n += 1
    return my_num


print(my_fib(10))

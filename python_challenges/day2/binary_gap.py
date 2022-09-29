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
print(my_num2)

for num in my_num[2:]:
    if int(num) == 0:
        my_other_count += 1
    else:
        if my_zero_count < my_other_count:
            my_zero_count = my_other_count
        my_other_count = 0
print(my_zero_count)


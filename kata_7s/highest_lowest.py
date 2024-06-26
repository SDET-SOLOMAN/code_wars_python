# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

def high_and_low(numbers):
    my_nums = numbers.split(" ")
    my_max = int(my_nums[0])
    my_min = int(my_nums[0])
    for num in my_nums:
        if int(num) > my_max:
            my_max = int(num)
        elif int(num) < my_min:
            my_min = int(num)
    return str(my_max) + " " + str(my_min)


def high_and_low2(numbers):
    my_list = [int(x) for x in numbers.split(" ")]
    my_max = my_list[0]
    my_min = my_list[0]

    for num in my_list:
        if num > my_max:
            my_max = num
        if num < my_min:
            my_min = num

    return str(my_max) + " " + str(my_min)


def high_and_low3(num):
    nums = sorted([int(s) for s in num.split()], reverse=True)
    return str(nums[0]) + " " + str(nums[-1])


def high_and_low4(numbers):
    numbers = [int(x) for x in numbers.split()]
    return str(max(numbers)) + " " + str(min(numbers))


def high_and_low5(numbers):
    numbers = sorted(list(map(lambda x: int(x), numbers.split())))
    return f"{numbers[-1]} {numbers[0]}"


def high_and_low6(numbers):
    my_list = sorted([int(x) for x in numbers.split()], reverse=True)
    return f"{my_list[0]} {my_list[-1]}"


def high_and_low7(numbers):
    n = sorted(map(int, numbers.split()))

    m1, m2 = n[0], n[-1]

    return f"{m2} {m1}"
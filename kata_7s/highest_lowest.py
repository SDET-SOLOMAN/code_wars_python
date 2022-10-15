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


print(sorted("bitcoin take over the world maybe who knows perhaps".split(), key=len))
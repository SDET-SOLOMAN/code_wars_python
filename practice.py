example = "ce32jvnfjnvffg4..4rf33fr3.4"
nums = []
temp = ''

for i, char in enumerate(example):
    print(temp, nums)
    if char.isdigit():
        temp += char
    elif char == '.' and "." not in temp:
        temp += char
    else:
        if temp:
            nums.append(temp)
        temp = ''
    if i == len(example) - 1 and temp:
        nums.append(temp)

total = sum(int(x) if "." not in x else float(x) for x in nums)
print(total)

def sum_of_numbers(string):
    total_sum = 0
    number = ''
    for char in string:
        if char.isdigit() or (char == '.'):
            number += char
        else:
            if number:
                total_sum += float(number)
                number = ''
    if number:
        total_sum += float(number)

    return total_sum
print(sum_of_numbers(example))
# Homework: Rewrite a program with any number of digits.
# Instead of  3 digits, you should sum digits up from n digits number,
# Where User enter n manually. n > 0

# user_input = int(input("Enter any num: "))
# my_num = 0
# if user_input > 0:
#     while user_input > 99:
#         my_num += user_input % 10
#         user_input = user_input // 10
#     my_num += user_input % 10
#     my_num += user_input // 10
# print(my_num)
#
# num1 = int(input("Num1= "))
# num2 = int(input("Num2= "))
# num3 = int(input("Num3= "))
#
# my_max = num1
#
# if my_max < num2:
#     my_max = num2
# if my_max < num3:
#     my_max = num3
# print(my_max)

# or max()

# Count odd and even numbers.  Count odd and even digits of the whole number. E.g,
# if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

nums = 34560
my_odds = []
my_evens = []

for num in str(nums):
    if int(num) % 2 == 0:
        my_evens.append(num)
    else:
        my_odds.append(num)
print(my_evens)
print(my_odds)

print(list(filter(lambda x: int(x) % 2 == 0, str(nums))))
print(list(filter(lambda x: int(x) % 2 != 0, str(nums))))


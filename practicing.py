# def move_zeros(lst):
#     new_num = []
#     second_num = []
#     for num in lst:
#         if num != 0:
#             new_num.append(num)
#         else:
#             second_num.append(0)
#     new_num.extend(second_num)
#     return new_num
#
# def create_phone_number(n):
#     first_bracket = "("
#     second_bracket = ")"
#     first_num = ''.join([str(x) for x in n[:3]])
#     second_num = ''.join([str(x) for x in n[3:6]])
#     third_num = ''.join([str(x) for x in n[6:]])
#     return first_bracket + first_num + second_bracket + " " + second_num + "-" + third_num
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

nums = ["23:11"]
for n in nums:
    n = n.split(":")
    print(n[0])
####### Signs ---------------------------------------


# all / any

def is_all_strings(lst):
    return all(type(l) == str for l in lst)




def nearest_sq(n):
    rounded_square = round(n ** (1/2))
    return rounded_square ** 2

# chr() for char
# != not equal to
# and
# or
# not
# in
# math.ceil highest num
# math.floor lowest num
# min()
# max()
# help('keywords')
# // floor division, 5 // 2 = 2
# % modulo 5 % 2 = 1 remainder
# .split(" ") vs .replace(" ", "" )
# .replace(" ", "         ")
# capitilize or string1[:1].upper() + string1[1:]
# random
# randomint
# round()
# enumerate()
# isdigit()
# .count()

####### Python writing ------------------------------

# camel_case for most variables
# ALL_CAPITALS for DON'T CHANGE VARS
# _do_not_toch_ aka dunder


####### Functions -----------------------------------

# round(2,2) or f"{num.:2f}"
# ranges(0,10) - up to 10, range(0:10:2) step size
# length +1
# count(3) how many times 3 in shows up
# index(3) first index of 3 index(3, 4) index of 3 after index 4
# random(0,1) random float
# capitilize() - first letter
# title all first letters

######## LISTS ---------
# append(x) last place insert
# extend ([1,2,3]) adss to list
# insert(-2, "X")
# remove(4) removes first 4 it finds
# pop() if empty last item, if index
# ''.join()
# split()
# reverse()
# sort()
# [1::2]
# [:9:2] up to 9 step 2
# swapping values my_list = [1, 2].... my_list[0], my_list[1] = my_list[1], my_list[0]
# shuffling
# .index()
# clear
# del
# .count



######## DICTIONARIES ----------
# .items() return key:value in tuple
# dict(zip())
# cat = dict(name="James", age=35, iscute=True) --> creating dict
# cat = {}.fromkeys(['name', 'age', 'iscute'], None) --> None
# name = "jack"
# cat[name]
# .clear()
# new_dict = old_dict.copy() --> makes a copy of dict
# pop() --> doesnt delete last one if left empty, pop(should have key in it)
# popitem() at random
# my_dict.update(dict2) <- taking k,v from a dict and adding to another dict
# get() or in
# 'nam' in dict.values()
# --------------
# {k:k**2 for k in range(8)}
# {k:v**3 for k,v in dict_.items()}
# -----------
# a = "ABC"
# b = "DEF"
# print({a[i]:b[i] for i in range(len(a))})
# ------------
# instructor = {'name':'james', 'number':'232', 'address': "vermont ave"}
# print({k[0].upper() + k[1:]:v[0].upper()+ v[1:] for k,v in instructor.items()})
# ----------
# nums = [1, 2, 3, 4, 5, 6]
# print({num:("X" if num % 2 == 0 else "O") for num in nums})
# ----------------------
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}
# answer = dict(person)

# def return_day(num):
#
#     my_dict = {
#         1: "Sunday",
#         2: "Monday",
#         3: "Tuesday",
#         4: "Wednesday",
#         5: "Thursday",
#         6:  "Friday",
#         7: "Saturday"
#     }
#
#     try:
#         return my_dict[num]
#     except KeyError:
#         return None

# '''
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# '''
#
# # flesh out multiple_letter count:
# def multiple_letter_count(stri):
#     return {x: stri.count(x) for x in stri}





####### TUPLES --------
# .count()
# .index()
# ENUMERATE
my_tuple = (1, 2, 3, "James", None, [], True, {"name":"Mike"}, 45, 32, 11)
for k, v in enumerate(my_tuple):
    print(k, v)


########S SETS -----
# set([1,2,3,4,4,2])
# floating around, no indexes
# s = set({1, 4, 5}) or s = {1, 4, 5} or s = set([1, 4, 5])
# 1 in s - True
# list_of_cities = ['LA', "LA", "NY","NY","DC"] <- len(set(list_of_cities)) unique values
# .add(6)
# .remove(6) <- shows error if its missing
# . discard(6) is better, doesn't throw an error
# .copy()
# .clear()
# .pop() pops first num

# frozenset()

#issubset() ->
set1 = {1, 3, "James"}
set2 = {1, 3, "James", 4, 5, 4}
# if set1 is sub of set2
print("SETTTTT")
print(set1.issubset(set2))

#issuperset->
set1 = {1, 3, "James"}
set2 = {1, 3, "James", 4, 5, 4}
print(set2.issuperset(set1))
# if set2 owns set1

#intersection ->
set1 = {1, 3, "James"}
set2 = {1, 3, "James", 4, 5, 4}
print(set2.intersection(set1))
# common values

#difference->
set1 = {1, 3, "James"}
set2 = {1, 3, "James", 4, 5, 4}
print(set2.difference(set1))
# difference values of set2 from set1

# symetric_difference->
set1 = {1, 3, "James", 99}
set2 = {1, 3, "James", 4, 5, 4}
print(set2.symmetric_difference(set1))
# all the differences between sets

####### ARGS AND KWARGS
# *args tuple
# **kwargs dictionary



####### LAMBDAS
square2 = lambda args: ["even" if num % 2 == 0 else "odd" for num in args]
print(square2([1, 3, 4, 2, 1, 2, 4, 5, 19, 12]))

####### MAP
nums = [1, 2, 3, 4, 5, 6]
doubles = map(lambda x: x*2, nums)

people = ['james', 'oscar', 'steph']
names = map(lambda people: people.upper(), people)
names = list(names)


#######FILtER
my_num = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda x: x % 2 == 0, my_num)))

my_tuple = (1, 2, 3, "James", None, [], True, {"name":"Mike"}, 45, 32, 11)
print(tuple(filter(lambda x: type(x) == int, my_tuple)))
print(tuple(filter(lambda x: isinstance(x, int), my_tuple)))

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum(filter(lambda x: isinstance(x, int), list_1)))
print(sum([x for x in list_1 if type(x) == int]))


# ZIP

mids = [80, 91, 78]
finals = [98, 89, 53]
names = ['huy', 'duy', 'lui']

print(dict(zip(names, [mids[i] if mids[i] > finals[i] else finals[i] for i in range(len(names))])))
# or
print(dict(zip(names, (max(x) for x in zip(mids, finals)))))
# or
print({x[0] : max(x[1], x[2]) for x in zip(names, finals, mids)})
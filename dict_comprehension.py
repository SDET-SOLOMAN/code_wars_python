donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = sum({a for a in donations.values()})
total_donations2 = sum(donations.values())

numbers = dict(first_num=20, second_num=40, third_num=55)
print({num ** 2 for num in numbers.values()})
print({k: num ** 2 for k, num in numbers.items()})

# making a dict from list
print({num: num ** 2 for num in range(0, 5)})

# going through strings and making a dict
str1 = 'ABC'
str2 = '123'
print({str1[i]: str2[i] for i in range(len(str1))})

# going throrugh dict and upper
instructor = dict(name='james', his_class='python', city='san-antonio', color='pink')
print({k.title() for k in instructor.keys()})

# going through list with odd or even
my_llist = [1, 2, 3, 4, 5, 6, 7]
print({i: ('Even' if i % 2 == 0 else 'Odd') for i in my_llist})

# zip
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, 3)}
dict(zip(list1, list2))

# ------

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
answer = {k: v for k, v in person}
answer = dict(person)

# -------
answer = {char: 0 for char in 'aeiou'}
answer = dict.fromkeys("aeiou", 0)

# -------
answer = {x: chr(x) for x in range(65, 91)}

# --------

user = [
    (0, "Bob", 'password'),
    (1, "James", 'password')
]

print({x[1]: x for x in user})
# DESCRIPTION:
# The following code was thought to be working properly, however when the code tries to access the age
# of the person instance it fails.
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
# For this exercise you need to fix the code so that it works correctly.
#
# Note: the order of the person's full name is first name and last name.


# found this solution in solutions
class Person3:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Person:

    def __init__(self, first_name, last_name, age):
        self.full_name = f"{first_name} {last_name}".strip()
        self.age = age


class Person1:

    def __init__(self, first_name, last_name, age):
        self.full_name = first_name + " " + last_name
        self.age = age

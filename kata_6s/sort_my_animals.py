# Consider the following class:
#
# class Animal:
#     def __init__(self, name, number_of_legs):
#         self.name = name
#         self.number_of_legs = number_of_legs
# Write a method that accepts a list of objects of type Animal, and returns a new list.
# The new list should be a copy of the original list, sorted first by the animal's number of legs, and then by its name.
#
# If an empty list is passed in, it should return an empty list back.

def sort_animals(lst: list) -> list:

    if not lst:
        return []
    sorted_list = sorted(lst, key=lambda animal: (animal.number_of_legs, animal.name))
    return sorted_list

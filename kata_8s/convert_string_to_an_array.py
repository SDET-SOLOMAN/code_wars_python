# Write a function to split a string and convert it into an array of words.
import six


# Examples (Input ==> Output):

# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    # return s.split(' ')
    return [x for x in s.split(" ")]


string_to_array2 = lambda s: s.split(" ")

print(string_to_array("James is the best guy for a role of Spider Man"))
print(string_to_array2("James is the best guy for a role of Spider Man"))


# without using split method

def string_to_array3(s):
    temp = []

    temp2 = ""

    for i, char in enumerate(s):

        if char != " ":
            temp2 += char

        elif char == " ":
            temp.append(temp2)
            temp2 = ""

        if i == len(s) - 1 and temp2:
            temp.append(temp2)

    return temp if s else [""]
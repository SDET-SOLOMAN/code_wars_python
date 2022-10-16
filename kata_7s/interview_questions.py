# You receive the name of a city as a string, and you need to return a string that shows how many times each letter
# shows up in the string by using asterisks (*).
#
# For example:
#
# "Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
# As you can see, the letter c is shown only once, but with 2 asterisks.
#
# The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no
# spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.
#
# Note that the return string must list the letters in order of their first appearance in the original string.
#
# More examples:
#
# "Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
# "Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
# Have fun! ;)

def get_strings(city):
    my_dict = dict()
    city = city.lower()
    for index in range(len(city)):
        if my_dict.get(city[index]):
            my_dict[city[index]] += "*"
        else:
            my_dict[city[index]] = '*'
    my_str = ''
    for k, v in my_dict.items():
        if k != " ":
            my_str += str(k)
            my_str += ":"
            my_str += str(v)
            my_str += ","
    return my_str[:-1]


def get_strings2(city):
    my_string = ''
    for num in city:
        if num.lower() not in my_string and num != " ":
            my_string += num.lower()
            my_string += ":"
            my_string += "*" * city.lower().count(num.lower())
            my_string += ","
    return my_string[:-1]

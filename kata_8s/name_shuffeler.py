# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)
# "john McClane" --> "McClane john"

def name_shuffler(str_):
    new_name = str_.split(" ")
    return new_name[1] + " " + new_name[0]
    #return ' '.join(str_.split(' ')[::-1])

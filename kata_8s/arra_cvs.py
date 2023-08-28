# Create a function that returns the CSV representation of a two-dimensional numeric array.
#
# Example:
#
# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]]
#
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'

def to_csv_text(array):
    return '\n'.join([','.join([str(x) for x in s]) for s in array])


to_csv_text2 = lambda array: '\n'.join([','.join([(str(letter)) for letter in x]) for x in array])


def to_csv_text3(array):
    text = ""
    for char in array:
        for i,c in enumerate(char):
            if i < len(char) - 1:
                text += str(c) + ","
            else:
                text += str(c)
        text += "\n"
    return text[:-1]
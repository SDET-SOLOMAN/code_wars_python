# You have two arguments: string - a string of random letters(only lowercase) and array - an array of strings(feelings).
# Your task is to return how many specific feelings are in the array.
#
# For example:
#
# string -> 'yliausoenvjw'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '3 feelings.' // 'awe', 'joy', 'love'
#
#
# string -> 'griefgriefgrief'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '1 feeling.' // 'grief'
#
#
# string -> 'abcdkasdfvkadf'
# array -> ['desire', 'joy', 'shame', 'longing', 'fear']
# output -> '0 feelings.'
# If the feeling can be formed once - plus one to the answer.
#
# If the feeling can be formed several times from different letters - plus one to the answer.
#
# Eeach letter in string participates in the formation of all feelings. 'angerw' -> 2 feelings: 'anger' and 'awe'.

def count_feelings(st, arr):
    st = {x: st.count(x) for x in st}

    n = []

    for num in arr:

        temp = {x: num.count(x) for x in num}
        t = True

        for k, v in temp.items():
            if k not in st or st[k] < v:
                t = False
                break
        if t:
            n.append("1")
    return f"{len(n)} feeling{'s' if len(n) != 1 else ''}."
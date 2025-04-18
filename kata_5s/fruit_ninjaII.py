# You are a fruit ninja, your skill is cut fruit. You cut some fruit by your knife in last kata.
# You want to know how many fruits have been successfully cut, so you need to count the number of fruits. For example:
#
# halfFruits=["app","le","pe","ar","ban","ana"]
# countFruits(halfFruits)={"apple":1,"pear":1,"banana":1}
# As you see, you should return an object that contains all fruits and its number. We only count the whole fruit,
# the excess will be ignored:
#
# halfFruits=["app","le","app","le","le","le"]
# countFruits(halfFruits)={"apple":2}  //two "le" has been ignored
# The fruit which are not uniformly cut will be ignored. That is, When the length of fruit's name is a even number,
# the length of two parts should equal; When the length of fruit's name is an odd number,
# the left part is 1 character longer than right part.
#
# halfFruits=["app","le","appl","e","ap","ple","ale","pp","bo","mb"]
# countFruits(halfFruits)={"apple":1}  //only "app","le" is what we want
# In order to make clear what is the fruit, you may need a list fruitsName. It's a preloaded variable,
# you can use it directly. e` :[
#
# Task
# Complete function countFruits that accepts an argument halfFruits. Returns the result in accordance
# with the rules above.
#

from preloaded import fruits_name


def count_fruits(hf):
    dic = {k: hf.count(k) for k in set(hf)}

    re = {}

    for char in fruits_name:
        char1 = char[:(len(char) + 1) // 2]
        char2 = char[(len(char) + 1) // 2:]

        if char1 in dic and char2 in dic:
            temp = min(dic[char1], dic[char2])
            if temp > 0:
                re[char] = temp
                dic[char1] -= temp
                dic[char2] -= temp

    return re

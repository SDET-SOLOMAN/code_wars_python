str1 = 'Ajnjsnfjsfjfasjbsfm sffisfj fs'.lower()
s1 = {k: str1.count(k) for k in str1}
s2 = {}

for char in str1:
    if s2.get(char):
        s2[char] += 1
    else:
        s2[char] = 1

for k, v in s2.items():
    if v == 1:
        print(k)
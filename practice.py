name = "shsicihuhv dvn duv hf wudhwudhw"
dict_name = {}

for s in name:
    if s in dict_name:
        dict_name[s] += 1
    else:
        dict_name[s] = 1
    print(dict_name)

for k, v in dict_name.items():
    if v == 1:
        print(k)
        break
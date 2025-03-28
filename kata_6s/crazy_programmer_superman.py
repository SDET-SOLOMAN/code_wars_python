# def find_super_man(s):
#     super = "SUPERMAN"
#     num = 8
#     s = s + "0"
#
#     for i, x in enumerate(s[:-1]):
#         if x.upper() in super and s[i + 1].upper() not in super:
#             num -= 1
#             super = super.replace(x.upper(), '')
#
#     return "Hi, SuperMan!" if num == 0 else "Are you crazy?"

def find_super_man(s):
    
    super = "SUPERMAN"
    num = 8
    s = s + "0"

    for i, x in enumerate(s[:-1]):
        if x.upper() in super and s[i + 1].upper() not in super:
            num -= 1
            super = super.replace(x.upper(), '')

    return "Hi, SuperMan!" if num == 0 else "Are you crazy?"
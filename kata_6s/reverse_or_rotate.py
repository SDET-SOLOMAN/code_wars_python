total = lambda nums: sum(int(ch) for ch in nums)
modulo = lambda x: x % 2 == 0


def rev_rot(s, sz):
    if sz <= 0 or not s or sz > len(s):
        return ""

    new = []
    for num in range(0, len(s), sz):
        temp = s[num:num + sz]
        if len(temp) == sz:
            new.append(temp)

    return "".join(
        x[::-1] if modulo(total(x)) else (x[1:] + x[0])
        for x in new
    )

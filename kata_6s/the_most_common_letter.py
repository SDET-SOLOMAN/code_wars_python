# Find the most common letter (not a space) in the given string (comprised of at least 3 lowercase words)
# and replace it with the given letter.
#
# If such letters are two or more, choose the one that appears earliest in the string.
#
# For example:
#
# ('my mom loves me as never did', 't') => 'ty tot loves te as never did'
# ('real talk bro', 'n') => 'neal talk bno'
# ('great job go ahead', 'k') => 'grekt job go khekd'

def replace_common(st, letter):
    x = {k: st.count(k) for k in st if k.isalpha()}

    temp = ("", 0)

    for k, v in x.items():
        if v > temp[1]:
            temp = (k, v)

    st = st.replace(temp[0], letter)
    return st
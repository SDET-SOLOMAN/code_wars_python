# Kata Task
# I have a cat and a dog.
#
# I got them at the same time as kitten/puppy. That was humanYears years ago.
#
# Return their respective ages now as [humanYears,catYears,dogYears]
#
# NOTES:
#
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


human_years_cat_years_dog_years3 = lambda hy: [hy, 16 + 4 * hy, 14 + 5 * hy] if hy > 1 else [1, 15, 15]


def human_years_cat_years_dog_years(hy):
    if hy < 0:
        return [0, 0, 0]
    elif hy < 2:
        return [hy, 15, 15]
    elif hy < 3:
        return [hy, 24, 24]
    h, c, d = hy, 24, 24
    for num in range(3, hy + 1):
        c += 4
        d += 5
    return [h, c, d]


def human_years_cat_years_dog_years2(hy):
    num = [hy]
    cat = 15
    dog = 15
    for n in range(1, hy + 1):
        if n >= 3:
            cat += 4
            dog += 5
        elif n == 2:
            cat += 9
            dog += 9
    num.append(cat)
    num.append(dog)
    return num
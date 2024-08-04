# Karan's company makes software that provides different features based on the version of operating system of the user.
#
# For finding which version is more recent, Karan uses the following method:
#
# While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the Operating system company
# just released OS version 10.10.
#
# Karan's function fails for the new version:

# compare_versions("11", "10");                    # returns True
# compare_versions("11", "11");                    # returns True
# compare_versions("10.4.6", "10.4");              # returns True
# compare_versions("10.4", "11");                  # returns False
# compare_versions("10.4", "10.10");               # returns False
# compare_versions("10.4.9", "10.5");              # returns False

def compare_versions(ver1, ver2):
    return [int(i) for i in ver1.split(".")] >= [int(i) for i in ver2.split(".")]


def compare_versions2(version1, version2):
    my_first = version1.split(".")
    my_second = version2.split(".")
    while len(my_second) < len(my_first):
        my_second.append('0')
    if len(version2) > len(version1):
        return False
    for num in range(len(my_first)):
        if my_first[num].isdigit() and my_second[num].isdigit():
            if int(my_first[num]) == int(my_second[num]):
                continue
            if int(my_first[num]) < int(my_second[num]):
                return False
    return True


def compare_versions3(v1, v2):
    if not v1 or not v2:
        return False

    v1, v2 = v1.split("."), v2.split(".")

    switcher = 1 if len(v1) > len(v2) else 0 if len(v1) == len(v2) else 2

    while switcher != 0:

        if switcher == 1:
            v2.append("0")

        elif switcher == 2:
            v1.append("0")

        switcher = 1 if len(v1) > len(v2) else 0 if len(v1) == len(v2) else 2

    for i, c in enumerate(v1):
        if int(c) < int(v2[i]):
            return False

    return True


def compare_versions4(v1, v2):

    v1 = v1.split(".")
    v2 = v2.split(".")

    while v1 and v2:

        if int(v1[0]) != int(v2[0]):
            return int(v1[0]) > int(v2[0])

        v1 = v1[1:]
        v2 = v2[1:]

    return len(v2) == 0


def compare_versions5(v1, v2):
    v1, v2 = v1.split("."), v2.split(".")
    l1 = len(v1)
    l2 = len(v2)
    cycle = True

    while cycle:

        if len(v1) == len(v2):
            cycle = False

        elif len(v1) > len(v2):
            v2.append("0")

        elif len(v2) > len(v1):
            v1.append("0")

    for num in range(len(v1)):
        if int(v1[num]) < int(v2[num]):
            return False
        elif int(v1[num]) > int(v2[num]):
            return True
    return True
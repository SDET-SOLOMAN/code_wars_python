# You are given two strings (st1, st2) as inputs. Your task is to return a string containing the numbers
# in st2 which are not in str1. Make sure the numbers are returned in ascending order.
# All inputs will be a string of numbers.
#
# Here are some examples:
#
# findAdded('4455446', '447555446666'); // '56667'
# findAdded('44554466', '447554466'); // '7'
# findAdded('9876521', '9876543211'); // '134'
# findAdded('678', '876'); // ''
# findAdded('678', '6'); // ''

def find_added(st1, st2):
    num1, num2 = st1, st2
    st1 = {k: (num1.count(k)) for k in num1}
    st2 = {k: (num2.count(k)) for k in num2}
    re = ""
    for k, v in st2.items():
        if k not in st1:
            re += k * v
        elif st1[k] < v:
            re += k * (v - st1[k])
    return "".join(map(str, sorted([int(x) for x in re])))


def findAdded2(st1, st2):
    return "".join(sorted(i * (st2.count(i)- st1.count(i)) for i in set(st2)))
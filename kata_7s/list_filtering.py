# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list


def filter2(l):
    return list(filter(lambda x: isinstance(x, int), l))


def filter3(l):
    return [x for x in l if type(x) == int]
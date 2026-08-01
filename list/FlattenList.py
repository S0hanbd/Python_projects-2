def flatten(l):
    x = []
    for i in l:
        if type(i) == list:
            x.extend(flatten(i))
        else :
            x.append(i)
    return x

print(flatten([1, [2, 3, [4, 5]], 6]))
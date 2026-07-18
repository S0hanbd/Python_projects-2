def removeDuplicates(l):
    x= []
    for i in l:
        if i not in x:
            x.append(i)

    return x


print(removeDuplicates([4, 2, 7, 2, 4, 9, 7]))
def leftshift(l):
    temp = l[-1]
    for i in range(len(l)-1,0,-1):
        l[i]= l[i-1]
    l[0] = temp

    return l

l = list(map(int,input("type numbers devided by comma: ").split(',')))

print(leftshift(l))
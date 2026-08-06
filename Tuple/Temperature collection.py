temp = (29, 31, 30, 28, 33, 32, 27)

s, maximum, minimum =0,temp[0],temp[0]


for i in temp :
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
    s += i

ave = s// len(temp)

print(maximum, minimum, ave)
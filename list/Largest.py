s = input("Inter numbers with spaces in between: ")
l = list(map(int, s.split()))

print(l)
s = set(l)
print(s)
max = l[0]
for i in l[1:] :
    if i > max:
        max = i


print(max)
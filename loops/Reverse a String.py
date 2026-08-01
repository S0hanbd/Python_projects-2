s = input("type a string: ")
s = list(s)
l = len(s)

for i in range(0,l//2):
    s[i],s[l-i-1] = s[l-i-1],s[i]

s = "".join(s)
print(s)
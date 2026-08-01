n = int(input("how many number you want to compare: "))
m : int = 0
for i in range(n):
    x = int(input("\n"))
    if x > m:
        m = x

print(f"the largest element is {m}")
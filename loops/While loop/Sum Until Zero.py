s =0
while True:
    temp = int(input("Add some number: "))
    if temp == 0:
        break
    s += temp

print(f"The total sum of all the numbers are: {s}")
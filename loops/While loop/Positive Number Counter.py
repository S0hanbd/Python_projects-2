s =0
while True:
    temp = int(input("number: "))
    if temp == -1:
        break
    if temp > 0:
        s += 1

print(f"The total number of positive number is: {s}")
n = int(input("type a positive number "))

s : int  = 0

for i in range(0,n+1,2):
    print(i,end= ' ')
    s += i

print(f"The sum of all even number is: {s}")


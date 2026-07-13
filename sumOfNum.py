n = int(input())
sum = 0
for i in range(1,n+1):
    if i != n:
        print(i,'+', end = '',sep='')
        sum += i
    else:
        print(i,'=', end='')
    sum = sum + i
    sum += i

print(sum)
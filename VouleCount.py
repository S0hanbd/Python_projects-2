st = str(input())
vouls = 'aeiouAEIOU'
count = 0
for c in st:
    if c in vouls:
        count += 1

print(count)
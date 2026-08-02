nums = list(map(int,input("type 10 Integers separeted by comma: ").split(',')))
result = []
for i in nums:
    if i not in result:
        result.append(i)
print(result)
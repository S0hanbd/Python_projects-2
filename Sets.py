set1 = {1,2,3,4,5,6,7,8,9}
set2 = {2,4,8,16}

result = {x for x in set1 if x not in set2 and x%2==0}
print(result)
print(type(result))
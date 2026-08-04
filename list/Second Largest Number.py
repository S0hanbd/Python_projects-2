l =list(map(int,input("Type a list of numbers devided by comma").split(",")))
largest = l[0]
second_largest = l[0]
for i in l:
    if i > largest:
        second_largest = largest
        largest = i
print(largest, second_largest)
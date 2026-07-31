a = int(input('type side a: '))
b = int(input('type side b: '))
c = int(input('type side c: '))

if a+b < c or a+c < b or b+c < a:
    print("not Triangle")
else:
    if a == b == c:
        print('Equilateral Triangle')
    elif a == b or b == c or c == a:
        print('Isosceles')
    elif a != b and b != c and c != a:
        print('Scalene Triangle')

def square()-> float:
    n = float( input("please enter a positive integer: "))
    return n * n

def cube()-> float:
    n = float( input("please enter a positive integer: "))
    return n * n * n
def recrengle()-> float:
    a = float( input("please enter the length of side A : "))
    b = float( input("please enter the length of side B : "))
    return a * b
def circle()-> float:
    n = float( input("please enter a positive integer: "))
    return 2 * 3.1416 * n * n

print("WELCOME TO AREA CALCULATOR")
z = True

while z:
    print(""" 
        What do you want to calculate?
        1 - square
        2 - cube
        3 - recengle
        4 - circle
        5 - exit
    """)
    i = input("please enter your choice: ")
    if i == "1":
        print('The Square is ',square())

    elif i == "2":
        print('The cube is ',cube())

    elif i == "3":
        print('Area is ',recrengle())

    elif i == "4":
        print('Area is ',circle())

    elif i == "5":
        z = False


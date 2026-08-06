def add_dic(d):
    temp = input("type the product name: ")
    d[temp]= input("Quantity of the product: ")


my_direct ={}
while True:
    n= int(input("""1 to add 
2 to see
3 to exit
: """))


    if n == 1:
        add_dic(my_direct)
    elif n==2:
        print(my_direct)
    elif n == 3:
        break
    else:
        continue
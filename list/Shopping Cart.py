cart = []
while True:
    n = int(input("""1 add element
2 remove item
3 desplay items
4 exit
"""))
    if n == 1:
        cart.append(input("type the name of product: "))
    elif n == 2:
        cart.pop(cart.index(input("The element you want to remove: ")))
    elif n == 3:
        print(cart)
    else:
        break
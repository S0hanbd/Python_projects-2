num = 61
iteration =0
while True:
    iteration += 1
    n = int(input("guess a Number: "))
    if num> n:
        print("Go Higher ")
    elif num < n:
        print("Go Lower")
    else:
        print(f"You correctly Guessed the Number in {iteration} tries ")
        break

withdrawal = 0.00

amount = float(input("type the amount: "))

while True:
    withdrawal = float(input("the withdrawal amount: "))
    if withdrawal < 0 or amount < withdrawal:
        print("type a Valid amount")
    else:
        break

amount -= withdrawal

print(f"The updated amount of the Bank Account: {amount}")


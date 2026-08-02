while True:
   print( """1. Check Balance
2. Deposit
3. Withdraw
4. Exit""")
   n = int(input("chose the menu code: "))
   if n == 1:
       print("Balance is 40000")
   elif n == 2:
       print("Deposit")
   elif n == 3:
       print("withdraw")
   elif n == 4:
       print("exiting")
       break


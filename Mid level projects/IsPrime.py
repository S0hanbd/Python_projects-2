import math


def prime(num : int) -> bool  :
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        else:
            return True

n = int( input("please enter a positive integer: "))

print(prime(n))
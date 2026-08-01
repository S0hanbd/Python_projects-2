def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print('The Factorial is : ',factorial(int(input('Please enter a positive integer: '))))
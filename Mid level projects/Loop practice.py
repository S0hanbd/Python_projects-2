import math


def main():
    #factorial()
    pattern1()

# print numbers from 1-10

def print_num():
    for i in range(0,int(input('type a number '))):
        print(str(i))


def sum():
    s = 0
    for i in range(int(input('type a number '))+1):
        s = s + i
    print(s)

def count_degit():
    s = int (input('type a number '))
    count = 0
    while s >= 1 :
        count = count + 1
        s = s //10
    print(count)


def reverse():
    s = int (input('type a number '))
    r= 0
    while s > 0:
        r = r*10
        r += s % 10
        s //= 10
    print(r)
def palindrome():
    s = input('type anything ')
    if s == s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
def multiplication_table():
    n = int(input('type a number '))
    for i in range(1,11):
        print(n, 'x' , i , '=', n*i )

def factorial():
    n = int(input('type a number '))
    fa= 1
    for i in range(1,n+1):
        fa = fa*i
    print(fa)
def pattern1():
    n = int(input('type a number '))
    for i in range(1,n+1):
        print(' '*(n-i),'*'*i)

def isprime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
        else:
            return True
    return None


main()
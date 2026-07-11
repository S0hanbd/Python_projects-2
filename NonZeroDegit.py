def sumAndMultiply( n):
    sum :int  = 0
    n = int(n)
    new : int= 0
    i :int =1
    while n > 0:
        if n%10 != 0:

            sum += n%10
            new += (n%10) * i
            i = i *10
        n = n//10

    return sum * new


print(sumAndMultiply(10203004))
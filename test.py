def number_pattern(n):
    if not isinstance(n, int):
        return ('n must be an integer')
        print('Argument must be an integer value.')
    elif n < 1:
        return('Argument must be an integer greater than 0.')
    pattern = ''
    for i in range(1,n+1):
        if i ==n:
            pattern += str(i)
        else:
            pattern += str(i) + ' '
    return pattern

print(number_pattern('ds'))
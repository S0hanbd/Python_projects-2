def palindrome(string):
    string = str(string)
    string2 = string[::-1]
    if string == string2:
        return "Number is palindrome"
    else:
        return "Number is not palindrome"


print(palindrome(input("Please enter a string: ")))
def isPalindrome(x):
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False
    
isPalindrome(121)
        
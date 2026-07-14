x = 2**31

def isPalindrome(x):

    # x int to str
    a = str(x)

    b = a[::-1]

    if (a == b):
        return True
    
    else:
        return False

print(isPalindrome(x))
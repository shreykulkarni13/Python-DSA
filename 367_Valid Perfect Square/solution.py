num = 16
def isPerfectSquare(num):
    ...
    s = (num)**(1/2)
    if (s%1 == 0):
        return True
    else: 
        return False
        

print(isPerfectSquare(num))

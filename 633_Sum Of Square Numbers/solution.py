c = 8

def judgeSquareSum(c):
    b = int(c**(1/2))
    # a**2 + b**2 = c
    

    if (c == 0):
        return True
    
    for a in range (0,b):
        if (a**2 == c - b**2):
            return True
        else:
            continue

    return False

        

print(judgeSquareSum(c))

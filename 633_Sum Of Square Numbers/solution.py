c = 74

def judgeSquareSum(c):
    s = int(c**(1/2)) + 1    #a**2 + b**2 =c
    map = {}
    for i in range (0,s):
        j = (c - i**2)**(1/2)
        if (j%1 == 0):
                return True
        else:
            continue
    return False

print(judgeSquareSum(c))

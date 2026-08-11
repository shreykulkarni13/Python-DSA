num = "11111"
t = 26

def smallestNumber(num, t):
    ...
    
    n = t
    while (n!=1):
        if (n%7 == 0):
            n = n//7
        elif (n%5 == 0):
            n = n//5
        elif (n%3 == 0):
            n = n//3
        elif (n%2 == 0):
            n = n//2
        else:
            return -1
    
    while True:
        map = {}
        l = len(num)
        product = 1
        for i in range (0,l):
            map[int(num[i])] = i
            product = product*int(num[i])
        
        if (0 in map):
            num = int(num)+1
            num = str(num)
            continue
        
        if(product%t == 0):
            return num
        else:
            num = int(num)+1
            num = str(num)

            continue
    
print(smallestNumber(num, t))

    
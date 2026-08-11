num = 1234
t = 256

def smallestNumber(num, t):
    ...
    temp = t
    while (temp%2 == 0 or temp%3 == 0 or temp%5 == 0 or temp%7== 0):
        if (temp%7 == 0):
            temp = temp//7
        elif (temp%5 == 0):
            temp = temp//5
        elif (temp%3 == 0):
            temp = temp//3
        elif (temp%2 == 0):
            temp = temp//2
        else:
            return -1
            
    while True:      
        s = str(num)
        l = len(s)
        map = {}
        product = 1
        for i in range (0,l):
            map[i] = int(s[i])

        for i in range (0,l):
            product = product*map[i]

        map2 = {value : key for key, value in map.items()}

        if (0 in map2):
            num = num+1
            continue
        
        if(product%t == 0):
            return num
            
        else:
            num = num+1
            continue
    
            
print(smallestNumber(num, t))
n = 15
t = 4
def smallestNumber(n,t):
    ...
    while True:
        u = n%10
        v = n//10
        
        if (t == 1):
            return n
        
        if(n<10):
            if(n%t == 0):
                return n
                True
            else:
                n = n+1
        else:
            if ((u*v)%t == 0):
                return n
                True
            else:
                n = n+1

print(smallestNumber(n,t))
            
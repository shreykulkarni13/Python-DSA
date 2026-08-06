n = 1
t = 2

def smallestNumber(n,t):
    # def check(n,t):
        u = n%10
        v = n//10
        if(t == 1):
             return n
        if (n < 10):
             if(n%t == 0):
                  return n
             else:
                  n = n+1
                  return smallestNumber(n,t)
        else:
            if ((u*v)%t == 0):
                return n
            else:
                n = n+1
                return smallestNumber(n,t)

print(smallestNumber(n,t))


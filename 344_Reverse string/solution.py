s = ["h","e","l","l","o"]

def reverseString(s):
    ...
    l = 0
    r = len(s)-1
    
    while (l<r):
        temp = s[r]
        s[r] = s[l]
        s[l] = temp
        l = l+1
        r = r-1
    return s
        
print(reverseString(s))

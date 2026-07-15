s = "anagram"
t = "nagaram"

def isAnagram(s,t):
    s = s.lower().replace(" " , "")
    t = t.lower().replace(" " , "")
    
    s1 = list(s)
    
    if (len(t) != len(s)):
        return False
    
    for i in range (0, len(t)):
        if (t[i] in s1):
            s1.remove(t[i])
        else:
            return False
    return True

print(isAnagram(s,t))

# time complexity O(n.m)
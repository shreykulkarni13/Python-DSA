s = "cat"
t = "rat"

def isAnagram(s,t):
    map1 = {}       #for s
    map2 = {}       #for t

    if (len(s) != len(t)):
        return False
    
    for i in range (0,len(s)):
        if (s[i] in map1):
            map1[s[i]] += 1
        else:
            map1.update({s[i] : 1})

        if (t[i] in map2):
            map2[t[i]] += 1
        else:
            map2.update({t[i] : 1})

    if (map1 == map2):
        return True
    else:
        return False

print(isAnagram(s,t))

        
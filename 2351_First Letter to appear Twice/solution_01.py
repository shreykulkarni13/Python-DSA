s = "abcdd"

def repeatedCharacter(s):
    ...
    map = {}
    
    for i in range (len(s)):
        ...
        if (s[i] in map ):
            return s[i]
        
        else : 
            map[s[i]] = 1
            
print(repeatedCharacter(s))
 
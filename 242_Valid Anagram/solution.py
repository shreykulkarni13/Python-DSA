s = 'U+0041'
t = 'U+0061'

def isAnagram(s,t):
    s1 = list(s)

    for i in range (0, len(t)):
        if (t[i] in s1):
            s1.remove(t[i])

        else:
            return False
    return True

print(isAnagram(s,t))
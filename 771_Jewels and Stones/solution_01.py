jewels = "z"
stones = "ZZ"

def numJewelsInStones(jewels, stones):
    ...
    map = {}
    count = 0
    
    for i in range (0, len(stones)):
        ...
        if (stones[i] in map):
            map[stones[i]] += 1
            
        else:
            map[stones[i]] = 1

    for i in range (0,len(jewels)):
        ...
        if (jewels[i] in map):
            count = count + map[jewels[i]]
            
        else:
            continue
        
    return count

print (numJewelsInStones(jewels, stones))
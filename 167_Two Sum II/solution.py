numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
    ...
    diff = {}
    
    for i in range (0, len(numbers)):
        b = target - numbers[i]
        if b in diff:
            return [diff[b], i+1]
        
        else:
            diff[numbers[i]] = i+1
            
    
print(twoSum(numbers, target))

# 16 Mins
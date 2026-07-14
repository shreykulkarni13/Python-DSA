nums = [3,0,1]

def missingNumber(nums):
    n = len(nums)
    map = {}        #element (key) :index (value)

    for i in range (0,len(nums)):
        map.update({nums[i] : i})

    for i in range (0,(n+1)):
        if (i in map):
            continue
        else:
            return i
        
print(missingNumber(nums))
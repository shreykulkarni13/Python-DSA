nums = [9,6,4,2,3,5,7,0,1]


def missingNumber(nums):
    n = len(nums)
    map = {}
    

    for i in range (0,(n)):
        map.update({i:nums[i]})
        if (i in map ):
            continue
        
        else:
            return i
        
print(missingNumber(nums))
        
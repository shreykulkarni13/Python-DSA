nums = [0,1,0,3,12]

def moveZeroes(nums):
    ...
    n = len(nums)
    l=0
    r = 1
    
    while (r<n):
        if(nums[r]==0):
            r = r+1
            l = l+1
        
        elif(nums[l]==0):
            (nums[l], nums[r]) = (nums[r], nums[l])
            l = l+1
            r = r+1
            
        else:
            l = l+1
            r = r+1
            
    return nums
print (moveZeroes(nums))

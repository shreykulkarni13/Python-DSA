nums = [1,3,5,6]
target = 7

def searchInsert(nums, target):
    ...
    low = 0
    high = len(nums)-1
    
    while (low <= high):
        ...
        mid = (low+high)//2
        
        if (nums[mid] == target):
            return mid
        
        elif (nums[mid] < target):
            low = low + 1
            
        else:
            high = high - 1
    return low


print(searchInsert(nums,target))
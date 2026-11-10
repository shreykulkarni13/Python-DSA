nums = [0,0,1]

def moveZeroes(nums):
    ...
    n = len(nums)
    count = 0
    for i in range (0,n):
        if (nums[i] == 0):
            count += 1
        
        else:
            continue
    
    i = 1
    while (i <= count):
        nums.append(0)
        nums.remove(0)
        i = i+1
    return nums
print (moveZeroes(nums))

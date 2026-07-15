nums = [1,1,0,1,1,1]

def findMaxConsecutiveOnes(nums):
    count = 0
    maxcount = 0
    
    for i in range (0,len(nums)):
        if (nums[i] == 1):
            count += 1
        else:
            maxcount = max(count, maxcount)
            count = 0
    if (count > maxcount):
        return count
    else :
        return maxcount
print(findMaxConsecutiveOnes(nums))
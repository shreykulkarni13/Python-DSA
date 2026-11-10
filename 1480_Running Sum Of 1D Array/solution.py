nums = [1,1,1,1,1]


def runningSum(nums):
    ...
    sum = 0
    n = len(nums)
    
    for i in range (0, n):
        sum = sum + nums[i]
        nums[i] = sum
    return nums

print(runningSum(nums))

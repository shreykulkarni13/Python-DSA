nums = [1]
def missingNumber(nums):
    actual_sum = 0
    current_sum = 0
    n = len(nums)

    #for actual sum:
    for i in range (0,(n+1)):
        actual_sum = actual_sum + i


    #for current sum:
    for i in range (0,n):
        current_sum = current_sum + nums[i]

    if (actual_sum != current_sum):
        a = actual_sum - current_sum
        return a 
    
print(missingNumber(nums))
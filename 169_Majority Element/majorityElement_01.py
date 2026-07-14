nums = [2,3,2,2,3,2,5]

def majorityElement(nums):
    for i in range(0,len(nums)):

        a = nums.count(nums[i])

        if (a >= round(len(nums)/2)):
            return nums[i]
            

        
print(majorityElement(nums))
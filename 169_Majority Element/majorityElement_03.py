nums = [1]
def majorityElement(nums):
    dict = {}

    for i in range (0,len(nums)):

        if (len(nums) == 1):
            return nums[i]
        
        if (nums[i] not in dict):
            dict.update({nums[i] : 1})

        else:
            dict.update({nums[i] : dict[nums[i]]+1})
            if (dict[nums[i]] > len(nums)/2):
                return nums[i]
            
        
print(majorityElement(nums))
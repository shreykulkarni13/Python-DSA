nums = [1,2,3,1]


def containsDuplicate(nums):
    dict = {}   # element(key) : count(value)
    for i in range (0, len(nums)):
        if (nums[i] not in dict):
            dict.update({nums[i] : 1})

        else:
            return True
    return False
        
print(containsDuplicate(nums))
nums = [7, 11, 13, 2]
target = 9


def twoSum(nums, target):
    map = {}

    for x in range (0, len(nums)):
        diff = target - nums[x]
        if (diff in map):
            return [map[diff], x]
        
        else:
            map.update({nums[x] : x})

        

print(twoSum(nums, target))

# using dictionary here time complexity is O(n)
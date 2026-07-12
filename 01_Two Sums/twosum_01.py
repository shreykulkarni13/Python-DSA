nums = [3, 2, 3]
target = 6
# x + y = target

def twoSum(nums, target):
    for x in range (0, len(nums)):
        y = target - nums[x]


        if (y in nums and nums.index(y) != x):
            return ([x, nums.index(y)])
            break
            

print(twoSum(nums, target))

# here time complexity is O(n^2)
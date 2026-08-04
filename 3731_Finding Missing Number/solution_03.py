nums = [1, 1, 5, 9, 12,25]
def findMissingElements(nums):
    map = {}
    for i in range (0, len(nums)):
        map[nums[i]] = i

    low = min(nums)
    high = max(nums)
    missing = []

    while (low < high):
        if (low in map):
            low = low+1
        else:
            missing.append(low)
            low = low+1

    return missing


print(findMissingElements(nums))
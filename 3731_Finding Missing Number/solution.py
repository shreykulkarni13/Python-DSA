nums = [1, 1, 5, 9]
def findMissingElements(nums):
    l = min(nums)
    h = max(nums)
    missing = []

    while (l<h):
        if (l in nums):
            l = l+1
            continue
        else:
            missing.append(l)
            l = l+1

    return missing

print(findMissingElements(nums))


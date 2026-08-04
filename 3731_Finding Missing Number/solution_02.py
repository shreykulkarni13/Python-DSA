nums = [1, 1, 5, 9]
def findMissingElements(nums):
    l = min(nums)
    h = max(nums)
    new = []

    for i in range (l,h+1):
        ...
        new.append(i)

    missing = list(set(new) - set(nums))
    


    return missing

print(findMissingElements(nums))


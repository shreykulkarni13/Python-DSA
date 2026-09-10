nums = [5,0,1,2,3,4]

def buildArray(nums):
    ...
    # ans[i] = nums[nums[i]]
    
    ans = []
    
    for i in range (len(nums)):
        a = nums[nums[i]]
        ans.append(a)
        
    return ans

print(buildArray(nums))
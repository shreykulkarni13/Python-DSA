nums = [2,2,1,1,1,2,2]

def majorityElement(nums):
    s = set(nums)
    l = list(s)
    for i in range (0,len(l)):

        a = nums.count(l[i])

        if (a >= round(len(nums)/2)):
            return l[i]
            

        
print(majorityElement(nums))
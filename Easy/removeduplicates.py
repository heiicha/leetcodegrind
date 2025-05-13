def removeDuplicates(nums):
    count = 0
    for i,num in enumerate(nums):
        while nums.count(num) > 1:
            del nums[i]
    for num in nums:
        count+=1


# better solution, using sets

def removeDuplicatesBetter(nums):
    ans = sorted(set(nums))
    k = len(ans)
    for i in range(0, k):
        nums[i] = list(ans)[i]
    return k
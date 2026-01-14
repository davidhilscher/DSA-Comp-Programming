"LC 53 - Dynamic Programming (DP)"

# returns int


def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0
    
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
        
    return maxSub



print(maxSubArray([1, -2, 4, -1, 3, 2]))
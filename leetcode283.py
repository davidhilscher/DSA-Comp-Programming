"LC 283, two pointers"


def movesZeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums



print(movesZeroes([0, 1, 0, 3, 12]))



"""
seen = {}

for i, v in enumerate(nums):
    complement = target - v
    if complement in seen:
        return seen[complement], i
    else:
        seen[v] = i
"""
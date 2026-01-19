""" LC 26 - Two Pointer """


def removeDuplicates(nums):
    l = 1 # holds place

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
               
    return l




print(removeDuplicates([1,1,2])) # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5

# harder/more abstract easy problem
""" LC 169 - Array/Greedy/Boyer-Moore Voting Algorithm """

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if candidate == num:
                    count += 1
            elif count == 0:
                candidate = num
                count += 1
            else:
                count -= 1

        return candidate
    
    

"""
nums = [3,2,3] # returns 3
nums = [2,2,1,1,1,2,2] # returns 2
"""

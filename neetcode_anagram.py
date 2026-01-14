"""neetcode anagram."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
sol = Solution()


if __name__ == '__main__':
    print(sol.isAnagram('ajm', 'jam'))
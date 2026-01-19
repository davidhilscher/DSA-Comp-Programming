""" LC 3 - Two-Pointer/Hash set """


def lengthOfLongestSubstring(s):
    l = 0 # left pointer
    maxCount = 0 # holds MAX substring
    seen = set() # set to check for duplicate

    for r in range(len(s)): # right in range...
        while s[r] in seen: # check for duplicate
            seen.remove(s[l]) # remove duplicate from beginning of set
            l += 1 # move pointer forward to find new longest substring

        seen.add(s[r]) # adds each char to set

        maxCount = max(maxCount, r - l + 1) # returns larger value: prior max or current window length

    return maxCount


print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("pwwkew")) # 3 
print(lengthOfLongestSubstring("bbbbb")) # 1
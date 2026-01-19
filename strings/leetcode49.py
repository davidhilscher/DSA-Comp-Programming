""" LC 49 - strings """
# one of the harder string problems I've seen. Never used defaultdict before

from collections import defaultdict # dict that defaults to __blank__ (list, 0, etc.)

def groupAnagrams(strs):
    anagrams = defaultdict(list) # dict that defaults to list 
        
    for s in strs:
        key = ''.join(sorted(s)) # sorts strs, then joins, if anagram, it's equal
        anagrams[key].append(s) # appends str to key in dict "anagrams"
        
    return list(anagrams.values()) # returns values of each key in "anagrams"



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# the above test case should return: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

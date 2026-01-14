""" LC 1456 - Two pointer (sliding window)"""


def maxVowels(s, k): # string and int
    le = len(s)
    count = 0
    vowels = ['a','e','i','o','u']
    
    for i in range(k):
        if s[i] in vowels:
            count += 1
            
        best_str = count
        
    for i in range(k, le):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
            
        best_str = max(best_str, count)
        
    return best_str


print(maxVowels('abciiidef', 3)) # substring "iii" has 3 vowel letters
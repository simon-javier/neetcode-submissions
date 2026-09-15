class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count_s = {}
        for char in s:
            if char in char_count_s:
                char_count_s[char] += 1
            else:
                char_count_s[char] = 1

        char_count_t = {}
        for char in t:
            if char in char_count_t:
                char_count_t[char] += 1
            else:
                char_count_t[char] = 1
        
        if char_count_s == char_count_t:
            return True
        return False
        

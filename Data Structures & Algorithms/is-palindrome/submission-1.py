class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ""
        for c in s:
            if c.isalnum():
                normalized += c.lower()
        
        lo = 0
        hi = len(normalized)

        while lo < hi:
            if normalized[lo] != normalized[hi - 1]:
                return False
            lo += 1
            hi -= 1
        
        return True
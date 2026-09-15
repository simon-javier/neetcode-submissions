class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowedChars = "abcdefghijklmnopqrstuvwxyz0123456789"
        normalized = ""
        for c in s:
            if c.lower() in allowedChars:
                normalized += c.lower()
        lo = 0
        hi = len(normalized)

        while lo < hi:
            if normalized[lo] != normalized[hi - 1]:
                return False
            lo += 1
            hi -= 1
        
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ""
        for c in s:
            if c.isalnum():
                normalized += c.lower()
        
        return normalized == normalized[::-1]
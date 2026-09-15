class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1

        while lo < hi:
            while lo < hi and not self.alphaNum(s[lo]):
                lo += 1
            while hi > lo and not self.alphaNum(s[hi]):
                hi -= 1
            
            if s[lo].lower() != s[hi].lower():
                return False

            lo, hi = lo + 1, hi - 1
        return True

    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        checker = {}

        for i in range(len(s)):
            checker[s[i]] = checker.get(s[i], 0) + 1
            checker[t[i]] = checker.get(t[i], 0) - 1

        for char in checker:
            if checker[char] != 0:
                return False
        return True
        
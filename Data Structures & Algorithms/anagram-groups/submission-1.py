from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        if not strs or len(strs) == 1:
            result.append(strs)
            return result

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - 97] += 1
            groups[tuple(count)].append(word)

        for group in groups.values():
            result.append(group)

        return result

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        result = []

        for word in strs:
            char_count = [0] * 26 
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            groups[tuple(char_count)].append(word)
        
        for group in groups.values():
            result.append(group)
        
        return result
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        max_val_idx = 0

        for i in range(len(nums)):
            num_counts[nums[i]] += 1
        
        sorted_num_counts = dict(sorted(num_counts.items(), key=lambda item: item[1], reverse=True))

        arr = []
        max_count = 0
        for key in sorted_num_counts.keys():
            if max_count < k:
                arr.append(key)
                max_count += 1

        return arr
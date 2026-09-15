from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key,val in num_counts.items():
            bucket[val].append(key) 
        
        
        top_k = []
        count = 0
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            if (len(top_k) < k):
                top_k += bucket[i]
                count += 1
            else:
                break
        
        return top_k
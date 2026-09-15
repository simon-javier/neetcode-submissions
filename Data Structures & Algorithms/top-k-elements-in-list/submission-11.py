class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key,val in num_counts.items():
            bucket[val].append(key) 
        
        
        top_k = []
        count = 0
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
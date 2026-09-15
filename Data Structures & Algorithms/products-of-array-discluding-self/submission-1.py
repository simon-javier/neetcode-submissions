class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1, 1, 2, 8]
        # suffix = [1, 6, 24, 48]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
            
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])
        return res
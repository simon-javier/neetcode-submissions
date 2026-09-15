class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        count = 1
        prev = sorted_nums[0]
        longest = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - 1 == prev:
                count += 1
                if count > longest:
                    longest = count
            elif sorted_nums[i] == prev:
                continue
            else:
                count = 1
            prev = sorted_nums[i]
        return longest
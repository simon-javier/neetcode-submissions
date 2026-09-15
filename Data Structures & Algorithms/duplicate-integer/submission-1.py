class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_checker = []

        for num in nums:
            if num in num_checker:
                return True
            else:
                num_checker.append(num)

        return False

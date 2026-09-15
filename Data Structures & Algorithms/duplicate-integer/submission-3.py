class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_checker = set()

        for num in nums:
            if num in num_checker:
                return True
            else:
                num_checker.add(num)

        return False

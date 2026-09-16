class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            while numbers[lo] + numbers[hi] > target:
                hi -= 1
            while numbers[lo] + numbers[hi] < target:
                lo += 1

            if numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]

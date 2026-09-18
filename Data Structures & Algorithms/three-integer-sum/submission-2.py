class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        checked = set()
        for i in range(len(nums)):
            target = -nums[i]

            lo, hi = i+1, len(nums)-1

            while lo < hi:
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    if (nums[lo], -target, nums[hi]) not in checked:
                        checked.add((nums[lo], -target, nums[hi]))
                        triplets.append([nums[lo], -target, nums[hi]])
                    lo += 1
                    hi -= 1
        return triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            lo, hi = i+1, len(nums)-1

            while lo < hi:
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    triplets.append([nums[lo], -target, nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
        return triplets

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # We want to do sliding window after some preprocessing

        maxRight = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], nums[i])
        
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[l] > maxRight[r]:
                l += 1
            res = max(res, r - l)


        return max(res, r - l)

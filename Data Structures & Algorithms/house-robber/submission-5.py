class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            tmp = max(prev2, prev1 + nums[i])
            prev1 = prev2
            prev2 = tmp
        return prev2
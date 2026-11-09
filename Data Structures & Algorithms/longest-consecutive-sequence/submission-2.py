class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for num in nums:
            if (num - 1) not in numSet:
                k = 0
                while num in numSet:
                    num += 1
                    k += 1
                
                res = max(res, k)
        
        return res
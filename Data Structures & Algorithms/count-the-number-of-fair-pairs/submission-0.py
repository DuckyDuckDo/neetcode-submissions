class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort() 
        def two_pointers(x):
            """
            Find total number of pairs that sum up to at most x
            """
            l = 0
            r = len(nums) - 1
            total = 0
            while l < r:
                if nums[l] + nums[r] <= x:
                    total += r-l
                    l += 1
                else:
                    r -= 1
            return total
        return two_pointers(upper) - two_pointers(lower - 1)
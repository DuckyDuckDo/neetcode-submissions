class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # We want to find the total pairs that add up to at most upper
        # And then subtract it from total pairs that add up to lower - 1

        nums.sort()
        def at_most(x):
            l, r = 0, len(nums) - 1
            total_pairs = 0
            while l < r:
                if nums[l] + nums[r] <= x:
                    total_pairs += r - l # this is because from l, we can add r - l distinct pairs that are less than x
                    l += 1
                else:
                    r -= 1
            return total_pairs
        return at_most(upper) - at_most(lower - 1)
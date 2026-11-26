class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(nums, l, r, target):
            # Function to find last index less than target
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = binary_search(nums, i + 1, len(nums) - 1, lower - nums[i] - 1)
            high = binary_search(nums, i + 1, len(nums) - 1, upper - nums[i])

            res += high - low

        return res
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        l = 0
        res = float('inf')
        r = max(nums)
        while l <= r:
            mid = (l + r) // 2
            pair_array = []
            i = 1
            while i < len(nums):
                if nums[i] - nums[i-1] <= mid:
                    pair_array.append((nums[i-1], nums[i]))
                    i += 1
                i += 1
                
            if len(pair_array) >= p:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
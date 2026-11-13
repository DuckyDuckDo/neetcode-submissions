class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_total = 0
        frequency_map = {0: 1}

        res = 0
        for num in nums:
            curr_total += num
            res += frequency_map.get(curr_total - k, 0)
            frequency_map[curr_total] = frequency_map.get(curr_total, 0) + 1

        return res
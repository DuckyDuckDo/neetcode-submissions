class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_total = 0
        res = 0 
        sum_frequencies = defaultdict(int)
        sum_frequencies[0] = 1

        for num in nums:
            curr_total += num
            if (curr_total - k) in sum_frequencies:
                res += sum_frequencies[curr_total - k]
            sum_frequencies[curr_total] += 1
        return res
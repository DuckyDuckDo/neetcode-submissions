class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        min_so_far = prices[0]

        for price in prices[1:]:
            min_so_far = min(min_so_far, price)
            res = max(res, price - min_so_far)
        return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2

            total_hrs = sum([x / mid if x % mid == 0 else x // mid + 1 for x in piles])

            if total_hrs > h:
                l = mid + 1
            else:
                r = mid - 1

        return l
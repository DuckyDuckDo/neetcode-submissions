class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        l = 1
        r = len(height) - 1

        res = 0
        while l <= r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)

            if maxL < maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1
        
        return res
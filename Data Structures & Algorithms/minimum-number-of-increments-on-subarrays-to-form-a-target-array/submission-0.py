class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        # Use a monotonic stack and at any point where there is an increasing value, just add the difference to result
        res = 0
        stack = [0]

        for num in target:
            if num > stack[-1]:
                res += num - stack[-1]
            stack.append(num)
        return res

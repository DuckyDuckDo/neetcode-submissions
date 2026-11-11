class Solution:
    def numSquares(self, n: int) -> int:
        choices = []

        i = 1
        while i**2 <= n:
            choices.append(i**2)
            i += 1
        
        # once choices is set up, It pretty much becomes coin change, how many coins add up to target
        dp = [i for i in range(n + 1)]
        for choice in choices:
            for j in range(len(dp)):
                if (j - choice) >= 0:
                    dp[j] = min(dp[j-choice] + 1, dp[j])
        
        return dp[-1]
        

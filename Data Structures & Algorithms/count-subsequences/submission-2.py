class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [1] * (len(s) + 1)

        for i in range(len(t)):
            row = [0] * (len(s) + 1)
            for j in range(1, len(s) + 1):
                if j >= 2 and s[j-1] == t[i] and s[j-1] == s[j - 2]:
                    row[j] = row[j-1] + prev[j-1]

                elif s[j-1] == t[i] and (j - 1) >= i:
                    row[j] = row[j - 1] + prev[j - 1]

                else:
                    row[j] = row[j - 1]
            prev = row
        return prev[-1]

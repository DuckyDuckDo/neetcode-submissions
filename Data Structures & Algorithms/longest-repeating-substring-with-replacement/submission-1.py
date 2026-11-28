class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l = 0

        char_frequency = {}
        for r in range(len(s)):
            char_frequency[s[r]] = char_frequency.get(s[r], 0) + 1

            if (r - l + 1) - max(char_frequency.values()) > k:
                char_frequency[s[l]] -= 1
                l += 1
            else:
                res = max(r- l + 1, res)
        
        return res
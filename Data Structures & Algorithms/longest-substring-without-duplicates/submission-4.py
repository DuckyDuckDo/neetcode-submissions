class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()

        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in hash_set:
                while l < r and s[l] != s[r]:
                    hash_set.remove(s[l])
                    l += 1
                
                while l < r and s[l] == s[r]:
                    hash_set.remove(s[l])
                    l += 1
                

            res = max(r - l + 1, res)    
            hash_set.add(s[r])

        return res
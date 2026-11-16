class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            alphabet_index = ord(s[i]) - ord('a')
            if first[alphabet_index] == -1:
                first[alphabet_index] = i
            last[alphabet_index] = i
    

        res = 0
        for i in range(len(first)):
            mids = set()
            first_index, last_index = first[i], last[i]
            if first_index != -1 and last_index != -1 and first_index != last_index:
                for mid in s[first_index + 1: last_index]:
                    mids.add(mid)
            
            res += len(mids)
        
        return res
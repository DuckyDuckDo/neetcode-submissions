class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(x) for x in strs])

        res = ""
        for i in range(min_length):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return res
            
            res += char
        
        return res
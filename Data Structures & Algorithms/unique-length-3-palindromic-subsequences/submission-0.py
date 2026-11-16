class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash_map_left = {}
        hash_map_right = {}

        char_set_left = set()
        for i in range(1, len(s)):
            char_set_left.add(s[i-1])
            hash_map_left[i] = char_set_left.copy()
        
        char_set_right = set()
        for i in range(len(s) - 2, -1, -1):
            char_set_right.add(s[i + 1])
            hash_map_right[i] = char_set_right.copy()
        
        res = set()
        for i in range(1, len(s) - 1):
            left = hash_map_left[i]
            right = hash_map_right[i]
            for char in left:
                if char in right:
                    res.add(f"{char}{s[i]}{char}")

        return len(res)
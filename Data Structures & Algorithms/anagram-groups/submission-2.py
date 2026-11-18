class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) # tuple of char frequencies -> words

        def get_char_frequencies(word):
            res = [0] * 26
            for char in word:
                res[ord(char) - ord('a')] += 1
            
            return tuple(res)
        
        for s in strs:
            char_frequencies = get_char_frequencies(s)
            hash_map[char_frequencies].append(s)
        
        return list(hash_map.values())
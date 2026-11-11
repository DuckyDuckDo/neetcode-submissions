class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # generate a hashmap that stores shifts as keys and string belonging to that shift as values
        hash_map = defaultdict(list)

        def calculate_shifts(s):
            res = tuple()
            for i in range(1, len(s)):
                res = res + ((ord(s[i]) - ord(s[i-1])) % 26,)
            return res
        
        for s in strings:
            shift = calculate_shifts(s)
            hash_map[shift].append(s)
        
        return list(hash_map.values())
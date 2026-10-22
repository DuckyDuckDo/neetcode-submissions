class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Just sliding window but with a length of 2 things

        fruit_dict = {}
        l = 0 
        res = 0

        for r in range(len(fruits)):
            fruit_dict[fruits[r]] = fruit_dict.get(fruits[r], 0) + 1

            while len(fruit_dict.keys()) > 2:
                fruit_dict[fruits[l]] -= 1
                if fruit_dict[fruits[l]] == 0:
                    del fruit_dict[fruits[l]]
                l += 1

            res = max(r - l + 1, res)
        
        return res


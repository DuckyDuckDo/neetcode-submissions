class Solution:
    def dividePlayers(self, skill: List[int]) -> int: 
        sum_of_team = min(skill) + max(skill)
        
        l = 0
        r = len(skill) - 1
        res = 0

        skill.sort()

        while l < r:
            if skill[l] + skill[r] != sum_of_team:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res
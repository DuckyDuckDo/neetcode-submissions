class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_map = {}
        curr_sum = 0

        res = 0
        for num in nums:
            curr_sum += num
            if (curr_sum - goal) in hash_map:
                res += hash_map[curr_sum - goal]
            if curr_sum == goal:
                res += 1
            hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1
        
        return res
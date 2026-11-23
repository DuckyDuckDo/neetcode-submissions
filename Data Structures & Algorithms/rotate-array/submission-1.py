class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            # Begin Cycling
            while True:
                next_index = (current + k) % len(nums)
                nums[next_index], prev = prev, nums[next_index]
                count += 1
                current = next_index

                if start == current:
                    break
    
            start += 1




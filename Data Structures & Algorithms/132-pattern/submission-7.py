class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We can use a stack that houses a number in nums, and the current minimum to the left of that number
        # If at any point we reach a number in num where the number is less than the top of the stack's number and greater than the current minimum at that number  , we found a 132 pair

        # So if nums[i] < stack[-1][0] and nums[i] > stack[-1][1] -> we found a solution
        # The first condition will be true because our stack is monotonic and we are always popping from the top 

        stack = [] # houses (num, curr_min so far up to num's index)
        curr_min = nums[0]

        # We don't really care about the first index, 
        for i in range(1, len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] > stack[-1][1]:
                return True
            
            # We update curr_min after because we don't want to include current index
            stack.append([nums[i], curr_min])
            curr_min = min(curr_min, nums[i])

        
        return False


            
            
            
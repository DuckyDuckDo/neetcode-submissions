class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)

            else:
                if not stack or close_to_open_map[char] != stack[-1]:
                    return False
                stack.pop()



        return len(stack) == 0
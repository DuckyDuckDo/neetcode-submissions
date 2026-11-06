class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        def reverse_integer(x):
            rev = 0
            while x > 0:
                digit = x % 10
                rev = (rev * 10) + digit
                x = x // 10
            return rev
        return reverse_integer(x) == x
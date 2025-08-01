class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert integer to string and check if it's the same when reversed
        return str(x) == str(x)[::-1]


sol = Solution()
print(sol.isPalindrome(121))    # True
print(sol.isPalindrome(-121))   # False
print(sol.isPalindrome(10))     # False

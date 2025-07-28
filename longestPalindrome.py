class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # return the valid palindrome

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            p1 = expandAroundCenter(i, i)
            # Even length palindrome
            p2 = expandAroundCenter(i, i + 1)

            # Update longest if found a longer one
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        # Traverse both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer in s if characters match
            j += 1      # Always move pointer in t

        # If we've gone through all characters in s, it's a subsequence
        return i == len(s)


s1 = "abc"
t1 = "ahbgdc"
print(Solution().isSubsequence(s1, t1))

s2 = "axc"
t2 = "ahbgdc"
print(Solution().isSubsequence(s2, t2))

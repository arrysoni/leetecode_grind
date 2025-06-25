class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        arr = []
        str = ''

        for i in range(len(s)):

            if s[i].isalnum():
                arr.append(s[i])
                str += s[i]

        print(str)

        if (arr == arr[::-1]):
            return True
        return False


s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)

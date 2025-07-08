class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s_length = len(s)
        s1 = s[:(s_length//2)]
        s2 = s[(s_length//2):]

        print("s1: ", s1)
        print("s2: ", s2)

        count1 = 0
        count2 = 0

        for char1 in s1:
            if (char1 == 'a' or char1 == 'e' or char1 == 'i' or char1 == 'o' or char1 == 'u'):
                count1 += 1

        for char2 in s2:
            if (char2 == 'a' or char2 == 'e' or char2 == 'i' or char2 == 'o' or char2 == 'u'):
                count2 += 1

        if (count1 == count2):
            return True
        else:
            return False


Solution().halvesAreAlike("book")
Solution().halvesAreAlike("textbook")

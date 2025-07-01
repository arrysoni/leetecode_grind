class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s) != len(t)):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        print('Sorted_s before: ', sorted_s)
        print('Sorted_t before: ', sorted_t)

        sorted_s = "".join(sorted_s)
        sorted_t = "".join(sorted_t)

        print('Sorted_s after: ', sorted_s)
        print('Sorted_t after: ', sorted_t)

        if (sorted_s == sorted_t):
            return True
        return False


s1 = "anagram"
t1 = "nagaram"
Solution().isAnagram(s1, t1)

s2 = "rat"
t2 = "car"
Solution().isAnagram(s2, t2)

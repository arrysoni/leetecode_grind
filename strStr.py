class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        substr = []  # will store a sliding window of chars
        m = len(needle)

        for idx, ch in enumerate(haystack):
            substr.append(ch)

            # keep window size at most m
            if len(substr) > m:
                substr.pop(0)

            # when window size matches needle length, compare
            if len(substr) == m:
                if self.isSame(substr, needle):
                    return idx - m + 1  # start index of the window

        return -1

    def isSame(self, substr, needle):
        return "".join(substr) == needle


haystack = "sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))  # 0

haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))  # -1

haystack = "aaaaa"
needle = "bba"
print(Solution().strStr(haystack, needle))  # -1

haystack = "mississippi"
needle = "issip"
print(Solution().strStr(haystack, needle))  # 4

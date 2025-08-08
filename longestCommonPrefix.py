class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the list of strings
        strs.sort()

        # Compare the first and last words only (they are most different)
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]


strs = ["flow", "flower", "flight"]
print(Solution().longestCommonPrefix(strs))

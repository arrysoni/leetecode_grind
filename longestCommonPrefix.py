class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        sorted_strs = strs.sort()
        shortest_word = strs[0]
        longest_prefix = ""

        for i in range(1, len(strs)):
            for j in range(len(shortest_word)):

                if (longest_prefix) == "":
                    if (shortest_word[j] == sorted_strs[i][j]):
                        longest_prefix += shortest_word[j]

                else:
                    for i in range(len(longest_prefix)):
                        if (longest_prefix[i] != sorted_strs[i][j]):
                            longest_prefix = longest_prefix[0:i]

        print(longest_prefix)
        return longest_prefix


strs = ["flow", "flower", "flight"]
print(Solution().longestCommonPrefix(strs))

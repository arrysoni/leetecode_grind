from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = defaultdict(list)
        result = []

        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)

        for value in anagrams.values():
            result.append(value)

        print(result)

        return result


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution().groupAnagrams(strs1)

strs2 = [""]
Solution().groupAnagrams(strs2)

strs3 = ["a"]
Solution().groupAnagrams(strs3)

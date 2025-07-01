class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initialize an empty dictionary to count how many times each character appears
        counts = {}
        for char in s:
            # For each character, get its current count (or 0 if not yet counted) and add 1
            counts[char] = counts.get(char, 0) + 1

        # Initialize the length of the longest possible palindrome
        longest = 0
        # Flag to check if there is at least one character with an odd count
        hasOdd = False

        # Go through the counts of each character
        for count in counts.values():

            # For each character, use as many pairs as possible (even count)
            # count // 2 gives number of pairs, *2 gives the total letters used in pairs
            longest += count // 2 * 2

            # If there is an odd leftover, mark that we can put one odd letter in the middle
            if count % 2 == 1:
                hasOdd = True

        # If any odd count was found, we can add one odd letter in the center
        if hasOdd:
            longest += 1

        # Return the length of the longest palindrome that can be formed
        print("The length of the longest palindrome that can be formed is: ", longest)
        return longest


s1 = "abccccdd"
Solution().longestPalindrome(s1)

s2 = "a"
Solution().longestPalindrome(s2)

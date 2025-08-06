class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_nums = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C':  100, 'D':  500, 'M':  1000}

        total = 0
        prev_value = 0

        # Traverse the string from right to left
        for char in reversed(s):
            value = roman_nums[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total


print(Solution().romanToInt("III"))  # Output: 3
print(Solution().romanToInt("LVIII"))  # Output: 58
print(Solution().romanToInt("MCMXCIV"))  # Output: 1994

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_nums = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C':  100, 'D':  500, 'M':  1000}

        reversed_string = s[::-1]
        sum = 0

        for left in range(0, len(s)-1):
            left_letter = reversed_string[left]
            print("left_letter: ",left_letter)
            for right in range(1, len(s)):
                right_letter = reversed_string[right]
                print("right_letter: ",right_letter)
                print("roman_nums[left_letter]:", roman_nums[left_letter])
                print("roman_nums[right_letter]", roman_nums[right_letter])
                if (roman_nums[left_letter] >= roman_nums[right_letter]):
                    sum = roman_nums[left_letter] + roman_nums[right_letter]
                else:
                    sum = roman_nums[left_letter] - roman_nums[right_letter]

        print(sum)
        return sum


Solution().romanToInt("III")

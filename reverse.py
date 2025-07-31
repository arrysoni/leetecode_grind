class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = 0

        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10

            if reversed_x > (INT_MAX - digit) // 10:
                return 0

            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x

# Test cases
test_cases = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),  # This should overflow and return 0
    (-2147483648, 0), # Also overflow when reversed
]

solution = Solution()

for i, (input_val, expected) in enumerate(test_cases):
    result = solution.reverse(input_val)
    print(f"Test Case {i + 1}: Input = {input_val}, Output = {result}, Expected = {expected}, {'✅' if result == expected else '❌'}")



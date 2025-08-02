class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Handle optional '+' or '-' sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Read digits and build the number
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow/underflow before it happens
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result


sol = Solution()
print(sol.myAtoi("42"))          # Output: 42
print(sol.myAtoi("   -042"))     # Output: -42
print(sol.myAtoi("1337c0d3"))    # Output: 1337
print(sol.myAtoi("0-1"))         # Output: 0
print(sol.myAtoi("words and 987"))  # Output: 0

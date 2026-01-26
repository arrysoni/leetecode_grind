import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        You cannot use without using multiplication, division, and mod operator.
        The integer division should truncate toward zero. 
        """
        """
        For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

        if quotient > (2^31) - 1:
            return (2^31) - 1

        if quotient < -(2^31):
            return -(2^31)
        """

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        while a >= b:
            temp = b
            multiple = 1

            # Double temp until it would exceed a
            while (temp << 1) <= a:
                temp <<= 1
                multiple <<= 1

            a -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        # Clamp (mostly unnecessary with overflow check above, but safe)
        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:
            return INT_MIN

        return quotient


dividend1 = 10
divisor1 = 3
print(Solution().divide(dividend1, divisor1))

dividend2 = 7
divisor2 = -3
print(Solution().divide(dividend2, divisor2))

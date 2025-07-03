class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0

        elif (n == 1):
            return 1

        else:
            return self.fib(n-1) + self.fib(n-2)


n1 = 2
print(Solution().fib(n1))

n2 = 3
print(Solution().fib(n2))

n3 = 4
print(Solution().fib(n3))

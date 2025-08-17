class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(cur, open_used, close_used):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if open_used < n:
                backtrack(cur + "(", open_used + 1, close_used)
            if close_used < open_used:
                backtrack(cur + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))
# ->["((()))","(()())","(())()","()(())","()()()"]

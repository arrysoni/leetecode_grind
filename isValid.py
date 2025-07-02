class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                # It's an opening bracket
                stack.append(char)
            elif char in mapping:
                # It's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Ignore non-bracket characters (optional)
                continue

        print(not stack)
        return not stack  # True if stack is empty


s1 = "()"
Solution().isValid(s1)

s2 = "()[]{}"
Solution().isValid(s2)

s3 = "(]"
Solution().isValid(s3)

s4 = "([])"
Solution().isValid(s3)

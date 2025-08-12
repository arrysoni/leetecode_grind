class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return

            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res


sol = Solution()
print(sol.letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

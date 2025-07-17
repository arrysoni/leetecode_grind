class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                if val in boxes[r // 3][c // 3]:
                    return False
                boxes[r // 3][c // 3].add(val)

        return True

class Solution(object):
    def isValidSudoku(self, board):
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):

            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()

                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int, current_board: List[str]):
            if row == n:
                result.append(current_board[:])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Create new row string with queen at position col
                new_row = '.' * col + 'Q' + '.' * (n - col - 1)

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, current_board + [new_row])

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0, [])
        return result
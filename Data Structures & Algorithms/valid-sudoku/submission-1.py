class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if (i,num) in seen or (num,j) in seen or (i//3,j//3,num) in seen:
                        return False

                    seen.add((i,num))
                    seen.add((num,j))
                    seen.add((i//3,j//3,num))

        return True
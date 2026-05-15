class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # maps row->val, val->col, and row//3|col//3 to val
        # we can't map val to col the same way, because it would cause problem
        # i.e we can't do 
        # seen.add((i,num))
        # seen.add((j,num))
        # because i and j will get equal in the loop, so we reverse the mapping for col and map val to col

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
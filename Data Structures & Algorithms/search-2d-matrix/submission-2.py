class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top , bot = 0, ROWS-1
        while top <=bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        
        if top>bot:
            return False

        l, r = 0, COLS-1
        row = (top+bot) //2
        while l<=r:
            m = l+ ((r-l) // 2)
            if matrix[row][m] > target:
                r= m-1
            elif matrix[row][m] < target:
                l = m+1
            else:
                return True
        
        return False
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []

        UP_WALL = 0
        DOWN_WALL = rows - 1
        LEFT_WALL = 0
        RIGHT_WALL = cols - 1

        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3

        current_direction = RIGHT
        i, j = 0, 0

        while len(res) < rows * cols:
            if current_direction == RIGHT:
                while j <= RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                j -= 1
                i += 1
                UP_WALL += 1
                current_direction = DOWN

            elif current_direction == DOWN:
                while i <= DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                RIGHT_WALL -= 1
                current_direction = LEFT

            elif current_direction == LEFT:
                while j >= LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                DOWN_WALL -= 1
                current_direction = UP

            elif current_direction == UP:
                while i >= UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                LEFT_WALL += 1
                current_direction = RIGHT

        return res
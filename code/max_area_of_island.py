class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def get_area(grid, row, column, rows, columns):
            if (row < 0 or column < 0 or row >= rows or column >=columns or grid[row][column] == 0):
                return 0

            grid[row][column] = 0

            left = get_area(grid, row, column -1, rows, columns)
            right = get_area(grid, row-1, column, rows, columns)
            up = get_area(grid, row + 1, column, rows, columns)
            down = get_area(grid, row, column + 1, rows, columns)

            return left + right + up + down + 1

        max_area = 0
        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if(grid[row][column] == 1):
                    area = get_area(grid, row, column, rows, columns)
                    max_area = max(area, max_area)

        return max_area;
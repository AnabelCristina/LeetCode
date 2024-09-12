class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def get_island(grid, row, column, rows, columns):
            if (row >= 0 and column >= 0 and row < rows and column < columns and grid[row][column] == "1"):
                grid[row][column] = 0

                left = get_island(grid, row, column -1, rows, columns)
                right = get_island(grid, row-1, column, rows, columns)
                up = get_island(grid, row + 1, column, rows, columns)
                down = get_island(grid, row, column + 1, rows, columns)


        islands = 0
        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if(grid[row][column] == "1"):
                    get_island(grid, row, column, rows, columns)
                    islands = islands + 1

        return islands
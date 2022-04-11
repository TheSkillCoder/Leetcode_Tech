class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        for iter in range(k):
            for i in range(m):
                for j in range(n-1, 0, -1):
                    grid[i][j], grid[i][j-1] = grid[i][j-1], grid[i][j]
            for i in range(m-1, 0, -1):
                grid[i][0], grid[i-1][0] = grid[i-1][0], grid[i][0]
        return grid
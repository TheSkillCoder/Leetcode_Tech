class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        stack = []
        for row in grid:
            stack += row
        stack = stack[-k:] + stack[:-k]
        
        return [stack[i * n: (i + 1) * n] for i in range(m)]
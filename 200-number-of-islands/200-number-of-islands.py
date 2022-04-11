class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        
        
        def dfs(x, y):

            nxt = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for i, j in nxt:
                if i>=0 and i<m and j>=0 and j<n and grid[i][j]=='1':
                    grid[i][j]=-1
                    dfs(i,j)
            
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ans+=1
                    dfs(i,j)
                    
        return ans
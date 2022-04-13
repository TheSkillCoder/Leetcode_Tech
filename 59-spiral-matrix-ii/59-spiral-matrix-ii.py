class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]*(n) for i in range(n)]
        val=1
        row_start, row_end, col_start, col_end = 0, n-1, 0, n-1
        while(row_start<=row_end and col_start<=col_end):
            for i in range(col_start, col_end+1):
                ans[row_start][i]=val
                val+=1
            row_start+=1
            
            for i in range(row_start, row_end+1):
                ans[i][col_end]=val
                val+=1
            col_end-=1
            
            for i in range(col_end, col_start-1, -1):
                ans[row_end][i]=val
                val+=1
            row_end-=1
            
            for i in range(row_end, row_start-1, -1):
                ans[i][col_start]=val
                val+=1
            col_start+=1
            
        return ans
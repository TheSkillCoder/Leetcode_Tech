class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def bs(row_num):
            i=0
            j=len(grid[row_num])-1
            ind=len(grid[row_num])
            while(i<=j):
                mid=(i+j)//2
                if grid[row_num][mid]<0:
                    ind=mid
                    j=mid-1
                else:
                    i=mid+1
            return len(grid[row_num])-ind
        
        ans=0
        for row_num in range(len(grid)):
            ans+=bs(row_num)
            
        return ans
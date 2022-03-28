class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        row_start, col_start = 0, 0
        row_end, col_end = len(matrix)-1, len(matrix[0])-1
        x=len(matrix)*len(matrix[0])
        while(True):
            
            if len(ans)==x:
                break
                
            if len(ans)<x:
                for i in range(col_start, col_end+1):
                    ans.append(matrix[row_start][i])
                row_start+=1
            if len(ans)<x:
                for i in range(row_start, row_end+1):
                    ans.append(matrix[i][col_end])
                col_end-=1
            if len(ans)<x:
                for i in range(col_end, col_start-1, -1):
                    ans.append(matrix[row_end][i])
                row_end-=1
            if len(ans)<x:
                for i in range(row_end, row_start-1, -1):
                    ans.append(matrix[i][col_start])
                col_start+=1
        return ans
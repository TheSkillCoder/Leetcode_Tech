class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0])-1
        
        while(True):
            if r>=len(matrix) or c<0:
                return False
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                c-=1
            elif matrix[r][c]<target:
                r+=1
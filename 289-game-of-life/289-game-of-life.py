class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(board, i, j):
            x=0
            if i>0 and j>0 and board[i-1][j-1]==1:
                x+=1
            if i<m-1 and j<n-1 and board[i+1][j+1]==1:
                x+=1
            if i>0 and board[i-1][j]==1:
                x+=1
            if j>0 and board[i][j-1]==1:
                x+=1
            if i<m-1 and board[i+1][j]==1:
                x+=1
            if j<n-1 and board[i][j+1]==1:
                x+=1
            if i<m-1 and j>0 and board[i+1][j-1]==1:
                x+=1
            if i>0 and j<n-1 and board[i-1][j+1]==1:
                x+=1
            return x
        
        hash_map=set()
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==0:
                    if count(board, i, j)==3:
                        hash_map.add((i,j)) 
                else:
                    if count(board, i, j)<2:
                        continue
                    elif count(board, i, j)==2 or count(board, i, j)==3:
                        hash_map.add((i,j))
                    elif count(board, i, j)>3:
                        continue
                        
        for i in range(m):
            for j in range(n):
                if (i,j) in hash_map:
                    board[i][j]=1
                else:
                    board[i][j]=0
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, i, j, ind, word):
            if ind==len(word):
                return True
            if i==-1 or i==m or j==-1 or j==n or word[ind]!=board[i][j]:
                return False
            temp=board[i][j]
            board[i][j]='*'
            found=dfs(board, i+1, j, ind+1, word) or dfs(board, i-1, j, ind+1, word) or dfs(board, i, j+1, ind+1, word) or dfs(board, i, j-1, ind+1, word)
            board[i][j]=temp
            return found
        
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfs(board, i, j, 0, word):
                    return True
        return False
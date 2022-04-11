class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        visited=set()
        
        def dfs(i, j):
            print(image)
            
            image[i][j] = newColor
            visited.add((i, j))
            nxt = [(i+1, j), (i-1, j), (i,j+1), (i, j-1)]
            for x, y in nxt:
                if x>=0 and x<m and y>=0 and y<n and (x, y) not in visited and image[x][y]==oldColor:
                    dfs(x, y)
                    
        dfs(sr, sc)
        return image
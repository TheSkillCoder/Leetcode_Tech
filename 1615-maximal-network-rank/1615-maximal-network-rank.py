class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        matrix=[[0 for i in range(n)] for i in range(n)]
        for i in roads:
            matrix[i[0]][i[1]]=1
            matrix[i[1]][i[0]]=1
            
        ans=0
        indeg={}
        for i in range(n):
            indeg[i]=0
        for i in roads:
            indeg[i[0]]+=1
            indeg[i[1]]+=1

        x = y = 0
        maxx = []
        for i in range(n):
            if indeg[i]>=indeg[x]:
                x=i
                maxx.append(i)
        for x in maxx:
            for i in range(n):
                if y==x and y+1<n:
                    y+=1
                if i!=x and indeg[i]>=indeg[y]:
                    y=i
                    ans = max(ans, (indeg[x]+indeg[y]-matrix[x][y]))

        return ans
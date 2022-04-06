class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x, y = tuple(edges[0])
        for i in range(1, len(edges)):
            m=edges[i]
            if m[0]==x:
                return x
            elif m[0]==y :
                return y
            elif m[1]==x:
                return x
            else:
                return y
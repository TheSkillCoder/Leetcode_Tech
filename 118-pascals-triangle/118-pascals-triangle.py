class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[]
        for i in range(n):
            lst=[1]*(i+1)
            for j in range(i-1):
                lst[j+1]=ans[-1][j]+ans[-1][j+1]
            ans.append(lst)
        return ans
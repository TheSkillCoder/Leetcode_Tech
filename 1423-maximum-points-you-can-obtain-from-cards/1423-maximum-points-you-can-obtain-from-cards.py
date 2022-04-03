class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=0
        for i in range(k):
            s+=cardPoints[i]
        ans=s
        i,j=k-1,len(cardPoints)-1
        while(i>=0):
            s+=cardPoints[j]
            s-=cardPoints[i]
            i-=1
            j-=1
            ans=max(s, ans)
        return ans
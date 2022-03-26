class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=prices[-1]
        ans=0
        for i in prices[::-1]:
            if i>maxx:
                maxx=i
            ans=max(ans, maxx-i)
        return ans
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[-1]*(k+1) for i in range(2)] for i in range(n)]

        def fun(ind, buy, cap):
            if ind==n or cap==0:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if(buy):
                dp[ind][buy][cap] = max((-prices[ind]+fun(ind+1, 0, cap)), fun(ind+1, 1, cap))
                return dp[ind][buy][cap]
            else:
                dp[ind][buy][cap] = max(prices[ind]+fun(ind+1, 1, cap-1), fun(ind+1, 0, cap))
                return dp[ind][buy][cap]
            
        return fun(0, 1, k)
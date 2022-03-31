class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={}
        x=ans=0
        for i in nums:
            x+=i
            if x == k:
                ans+=1
            if True:
                val=x-k
                if val in prefix_sum:
                    ans+=prefix_sum[val]
            prefix_sum[x]=prefix_sum.get(x,0)+1
        return ans
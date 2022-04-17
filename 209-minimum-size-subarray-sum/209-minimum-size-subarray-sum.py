class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        i=j=smm=flag=0
        ans=float("inf")
        while(i<=j):
            if smm>target:
                ans = min(ans, j-i)
                smm-=nums[i]
                i+=1
            elif (smm<target or flag==1) and j<len(nums):
                smm+=nums[j]
                j+=1
                flag=0
            elif smm==target and flag==0:
                ans = min(ans, j-i)
                flag=1
            else:
                i+=1
        return ans
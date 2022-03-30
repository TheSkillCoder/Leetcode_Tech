import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=math.inf
        k=0
        nums.sort()
        n=len(nums)
        while(k<n-2):
            i=k+1
            j=len(nums)-1
            while(i<j):
                x=nums[k]+nums[i]+nums[j]
                if x==target:
                    ans=target
                    return ans
                elif x>target:
                    j-=1
                elif x<target:
                    i+=1
                if abs(target-x)<abs(target-ans):
                    ans=x
            k+=1
        return ans
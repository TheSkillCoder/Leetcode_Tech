class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        x=0
        ans=set()
        nums.sort()
        n=len(nums)
        while(x<n-3):
            k=x+1
            while(k<n-2):
                i=k+1
                j=len(nums)-1
                while(i<j):
                    s=nums[x]+nums[k]+nums[i]+nums[j]
                    if s==target:
                        ans.add((nums[x], nums[k], nums[i], nums[j]))
                        j-=1
                        i+=1
                    elif s>target:
                        j-=1
                    elif s<target:
                        i+=1
                k+=1
            x+=1
        return ans
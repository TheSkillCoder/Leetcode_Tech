class Solution:
    
    def bs(self, target, i, nums):
        j=len(nums)-1
        i=i+1
        while(i<=j):
            mid=(i+j)//2
            if i==j and nums[mid]!=target:
                break
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return False
    
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=set()
        for i in range(len(nums)-1):
            x=self.bs(nums[i]+k, i, nums)
            if x==True:
                ans.add((nums[i], nums[i]+k))
        return len(ans)
                
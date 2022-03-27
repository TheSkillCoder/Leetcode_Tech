class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        n=len(nums)
        for i in range(n):
            if nums[i]>=0:
                break
        j=i-1
        while(i<n and  j>=0):
            if abs(nums[j])>nums[i]:
                ans.append(nums[i]*nums[i])
                i+=1
            else:
                ans.append(nums[j]*nums[j])
                j-=1

        while(i<n):
            ans.append(nums[i]*nums[i])
            i+=1
        while(j>=0):
            ans.append(nums[j]*nums[j])
            j-=1
            
        return ans
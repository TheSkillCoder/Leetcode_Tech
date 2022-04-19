class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while(i<j):
            while(i<j and j>=0 and nums[j]==val):
                j=j-1
            if nums[i]==val:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            i+=1
        for i in range(len(nums)):
            if nums[i]==val:
                i-=1
                break      
        return i+1
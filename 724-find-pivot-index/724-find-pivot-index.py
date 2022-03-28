class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        x=0
        for i in range(len(nums)):
            s-=nums[i]
            if s==x:
                return i
            x+=nums[i]
        return -1
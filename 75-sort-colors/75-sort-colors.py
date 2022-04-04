class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = -1, len(nums)
        k=0
        while(i<=k<j):
            if (nums[k]==1 or i==k):
                k+=1
            elif nums[k]==2:
                j-=1
                nums[k], nums[j] = nums[j], nums[k]
            elif nums[k]==0:
                i+=1
                nums[k], nums[i] = nums[i], nums[k]            
        return nums
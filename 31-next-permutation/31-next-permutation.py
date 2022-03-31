class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind1=i
                break
        else:
            for i in range(n//2):
                nums[i],nums[n-1-i]=nums[len(nums)-1-i],nums[i]
            return nums
        for j in range(n-1,ind1,-1):
            if nums[ind1]<nums[j]:
                ind2=j
                break
        nums[ind1], nums[ind2]=nums[ind2], nums[ind1]
        ind1+=1
        n-=1
        while(ind1<n):
            nums[ind1], nums[n] = nums[n], nums[ind1]
            ind1+=1
            n-=1
        return nums
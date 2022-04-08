class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=max(nums)
        s=set()
        for i in nums:
            if i>0:
                s.add(i)
        for i in range(1, n):
            if i not in s:
                return i
        if n>0:
            return n+1
        return 1
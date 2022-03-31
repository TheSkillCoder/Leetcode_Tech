class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        hash_map={}
        for i in range(n):
            hash_map[i] = 0
        for j in nums:
            hash_map[j]+=1
            if hash_map[j]>1:
                return j
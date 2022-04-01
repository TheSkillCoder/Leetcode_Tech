class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap={}
        ans=[]
        for i in nums:
            hashmap[i]=hashmap.get(i, 0)+1
        for i in hashmap:
            if hashmap[i]>1:
                ans.append(i)
        return ans
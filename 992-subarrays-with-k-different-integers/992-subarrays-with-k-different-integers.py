class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def fun(nums, k):
            if k==0:
                return 0
            hash_map={}
            l=r=at_most_k=0
            while(r<len(nums)):
                hash_map[nums[r]]=hash_map.get(nums[r], 0)+1
                while(len(hash_map)>k):
                    hash_map[nums[l]]-=1
                    if hash_map[nums[l]]==0:
                        hash_map.pop(nums[l])
                    l+=1
                at_most_k+=(r-l+1)
                r+=1
            return at_most_k
        
        ans = fun(nums, k)-fun(nums, k-1)
        return ans
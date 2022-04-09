class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i, 0)+1
        hash_arr=[]
        for i in hash_map:
            hash_arr.append([-hash_map[i], i])
        heapq.heapify(hash_arr)
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(hash_arr)[1])
        return ans
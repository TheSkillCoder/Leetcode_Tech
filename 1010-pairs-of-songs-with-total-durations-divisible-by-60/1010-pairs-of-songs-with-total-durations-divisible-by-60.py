class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_map={}
        ans=0
        for i in range(60):
            hash_map[i]=0
        for i in time:
            hash_map[i%60]+=1
        ans = ans + (hash_map[0]*(hash_map[0]-1))//2 + (hash_map[30]*(hash_map[30]-1))//2
        for i in range(1,30):
            ans+=(hash_map[i]*hash_map[60-i])
        return ans            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map={}
        l=r=0
        ans=0
        maxf=0
        while(r<len(s)):
            hash_map[s[r]]=hash_map.get(s[r], 0)+1
            maxf=max(maxf, hash_map[s[r]])
            while((r-l+1)-maxf)>k:
                hash_map[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans
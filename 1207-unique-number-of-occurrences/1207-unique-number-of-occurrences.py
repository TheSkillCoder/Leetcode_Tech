class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans={}
        flag=0
        for i in arr:
            ans[i]=ans.get(i, 0)+1
        arr = list(ans.values())
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                break
        else:
            return True
        return False
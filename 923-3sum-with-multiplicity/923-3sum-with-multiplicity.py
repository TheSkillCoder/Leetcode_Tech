class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        hsh={}
        for i in arr:
            hsh[i]=hsh.get(i, 0)+1
            
        answers=set()
        ans=0
        arr.sort()
        k=0
        n=len(arr)

        while(k<n-2):
            if arr[k]>target:
                break
            if k!=0 and arr[k-1]==arr[k]:
                k+=1
                continue
            i, j = k+1, n-1
            while(i<j):
                if arr[i]+arr[j]+arr[k]==target:
                    answers.add((arr[i], arr[j], arr[k]))
                    i+=1
                    j-=1
                elif arr[i]+arr[j]+arr[k]>target:
                    j-=1
                else:
                    i+=1
            k+=1
        
        for item in answers:
            x, y, z = item
            if x!=y and y!=z and z!=x:
                ans+=(hsh[x]*hsh[y]*hsh[z])
            elif x == y and y!=z:
                ans+=((hsh[x]*(hsh[x]-1))//2)*hsh[z]
            elif x==z and y!=x:
                ans+=((hsh[x]*(hsh[x]-1))//2)*hsh[y]
            elif x != y and y==z:
                ans+=((hsh[y]*(hsh[y]-1))//2)*hsh[x]
            else:
                ans += (hsh[x]*(hsh[x]-1)*(hsh[x]-2))//6
        return ans%(10**9 + 7)
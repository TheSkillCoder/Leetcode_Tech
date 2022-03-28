class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        i=0
        j=i+1
        ans=[intervals[i]]
        
        while(j<len(intervals)):
            if intervals[j][0]>ans[i][1]:
                ans.append(intervals[j])
                j+=1
                i+=1

            else:
                x=intervals[j][0]
                while i>=0 and ans[i][1]>=intervals[j][0]:
                    x=min(ans[i][0], x)
                    ans.pop()
                    i-=1
                ans.append([x,intervals[j][1]])
                i+=1
                j+=1
                
        return ans
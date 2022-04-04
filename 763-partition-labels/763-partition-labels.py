class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i, i]
            else:
                d[s[i]][1] = i

        intervals = list(d.values())
        intervals.sort()
        
        new_intervals = []
        x, y = -1, -1
        for i, j in intervals:
            if x == -1:
                x, y = i, j
            elif j <= y:
                continue
            elif i <= y:
                y = j
            else:
                new_intervals.append([x, y])
                x, y = i, j
        new_intervals.append([x, y]) 
        
        res = []
        for i, j in new_intervals:
            res.append(j-i+1)

        return res
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def valid_fun(capacity):
            total = 0
            dayss = 1
            for i in weights:
                if i > capacity:
                    return False
                total = total + i
                if total>capacity:
                    total = i
                    dayss+=1
            return (dayss<=days)
        
        start = 1
        end = sum(weights)
        while(start<end):
            mid = (start+end)//2
            if(valid_fun(mid)):
                end = mid
            else:
                start = mid+1
        return start
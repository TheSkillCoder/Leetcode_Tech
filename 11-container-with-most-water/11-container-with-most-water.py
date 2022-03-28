class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = maxarea = h = 0
        j = len(height)-1
        while i < j:
            h1 = height[i] 
            h2 = height[j]
            b1 = (j-i)
                
            if h1 > h2:
                area = h2 * b1
                j-=1
            else:
                area = h1 * b1
                i+=1
                
            maxarea = max(maxarea, area)
        
        return maxarea
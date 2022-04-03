class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def nselfun(heights):
            nsel=[-1]*len(heights)
            stack=[-1]
            for i in range(len(heights)):
                while(len(stack)>1 and heights[i]<=heights[stack[-1]]):
                    stack.pop()
                nsel[i]=stack[-1]
                stack.append(i)
            return nsel

        def nserfun(heights):
            nser=[0]*len(heights)
            stack=[len(heights)]
            for i in range(len(heights)-1, -1, -1):
                while(len(stack)>1 and heights[i]<=heights[stack[-1]]):
                    stack.pop()
                nser[i]=stack[-1]
                stack.append(i)
            return nser
        
        nsel = nselfun(heights)
        nser = nserfun(heights)

        ans=0
        for i in range(len(heights)):
            ans=max(ans, heights[i]*(nser[i]-nsel[i]-1))
        return ans
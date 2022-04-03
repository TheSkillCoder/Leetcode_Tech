class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        x, y = horizontalCuts[0], verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            x=max(x, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            y=max(y, verticalCuts[i]-verticalCuts[i-1])
        return (x*y)%(10**9+7)
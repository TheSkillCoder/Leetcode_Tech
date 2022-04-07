import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)
        while(len(stones)>1):
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, -(abs((-x)-(-y))))
        return -(stones[0])
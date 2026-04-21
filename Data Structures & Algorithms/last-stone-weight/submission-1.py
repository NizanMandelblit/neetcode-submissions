class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones] 
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first,second = abs(heapq.heappop(maxHeap)), abs(heapq.heappop(maxHeap))
            if first > second:
                heapq.heappush(maxHeap, -1*(first-second))
        maxHeap.append(0)
        return abs(maxHeap[0])
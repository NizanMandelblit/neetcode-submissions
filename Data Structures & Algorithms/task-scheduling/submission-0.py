class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  # task:frequency

        maxHeap = [-cnt for cnt in count.values()]  # most frequent task
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # paris of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                newCnt = 1 + heapq.heappop(maxHeap)  # cnt 0s -.. so +1
                if newCnt:
                    q.append([newCnt, n + time])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

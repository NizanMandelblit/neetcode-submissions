from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # Use a max-heap to always pick the task with the highest remaining frequency
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # stores pairs of [-remaining_cnt, available_at_time]

        while maxHeap or q:
            time += 1

            if maxHeap:
                # Pop the most frequent task and decrement its count
                # (Since it's negative, adding 1 brings it closer to 0)
                cnt = heapq.heappop(maxHeap) + 1

                # If there are still instances of this task left,
                # put it in the cooling queue
                if cnt != 0:
                    q.append([cnt, time + n])

            # Check if any task in the queue has finished its cooling period
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

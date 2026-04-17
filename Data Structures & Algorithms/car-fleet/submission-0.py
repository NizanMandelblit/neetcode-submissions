class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]  # one list of p,s
        pair.sort(reverse=True)  # reverse in ascending order based on position
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)  # what time will it reach target
            if (
                len(stack) >= 2 and stack[-1] <= stack[-2]
            ):  # if car behind reached target before car 1 then it's a fleet, and first car speeds is the one we account for the next car
                stack.pop()
        return len(stack)

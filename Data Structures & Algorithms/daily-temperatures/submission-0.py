class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            j=i+1
            count = 0
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    count = j-i # distance of j from i...
                    break
                j+=1
            if count:
                res.append(count)
            else:
                res.append(0)
        return res
            
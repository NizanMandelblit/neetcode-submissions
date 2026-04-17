class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force O(n^2)
        # res = []

        # for i in range(len(temperatures)):
        #     j = i + 1
        #     count = 0
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             count = j - i  # distance of j from i...
        #             break
        #         j += 1
        #     if count:
        #         res.append(count)
        #     else:
        #         res.append(0)
        # return res

        # stack

        res = [0]*len(temperatures)
        stack = [] # pairs of temp:index

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp_poped,i_poped = stack.pop()
                res[i_poped] = i- i_poped

            stack.append((temp,i)) 
        return res

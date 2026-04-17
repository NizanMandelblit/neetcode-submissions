class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force O(n^2)
        # res = 0
        # for i in range(len(s)):
        #     freqMap = {}  # freq of each char in the substring window
        #     maxf = 0  # value of the most freq char in the substring window
        #     for j in range(i, len(s)):
        #         freqMap[s[j]] = freqMap.get(s[j], 0) + 1
        #         maxf = max(maxf, freqMap[s[j]])
        #         if (j - i + 1) - maxf <= k:  # window size-maxf
        #             res = max(res, j - i + 1)
        # return res
        res = 0
        charSet = set(s)

        for c in charSet:
            l, count = 0, 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)

        return res

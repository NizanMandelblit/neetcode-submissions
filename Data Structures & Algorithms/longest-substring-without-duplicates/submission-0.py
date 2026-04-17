class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force O(n*m)
        res =0
        for i in range(0,len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res = max(res, len(seen))
            
        return res
                
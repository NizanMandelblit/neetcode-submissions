class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                res+=self.isPali(s[i:j])

        return res



    def isPali(self, s):
        l,r= 0, len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return 0
            r-=1
            l+=1

        return 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # # naive : o(nlogn time/ o(1) space (assuming heapsort))
        # return sorted(s) == sorted(t)

        # HashMap: O(1) time/O(n) space
        hashMapS = {}
        hashMapt = {}
        for c in s:
            hashMapS[c]= 1 + hashMapS.get(c, 0)
        for c in t:
            hashMapt[c]= 1 + hashMapt.get(c, 0)
        return hashMapS==hashMapt
            

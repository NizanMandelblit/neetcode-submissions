class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force check every substring of s2 and sort+comapre with sorted s1
        # Time Complexity  O(n^3 log n)$:
        # O(n^2) to find every substring
        # sort: O(n \log n) to sort each substring every time you find one.
        # s1Sorted= sorted(s1)
        # for i in range(len(s2)):
        #     subString=s2[i]
        #     for j in range(i+1,len(s2)):
        #         subString+=s2[j]
        #         if sorted(subString) == s1Sorted:
        #             return True
        # return False


        # hashmap
        count1= {} # frequency map count1 for all characters in s1.
        for c in s1:
            count1[c] = count1.get(c,0)+1
        need = len(set(s1)) # the number of unique characters in s1 whose counts must match.
        for i in range(len(s2)):
            count2 = {}
            cur=0
            for j in range(i,len(s2)):
                count2[s2[j]] = count2.get(s2[j],0) + 1
                if count2[s2[j]] > count1.get(s2[j],0):
                    break
                elif count2[s2[j]] == count1[s2[j]]:
                    cur+=1
                if cur==need:
                    return True
        return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversing the string
        # O(n) time and space
        # newStr= ''
        # for c in s:
        #     if c.isalnum():
        #         newStr+=c.lower()
        
        # return newStr==newStr[::-1]

        # two pointers O(n) time and O(1) space
        l, r = 0, len(s)-1
        while l<r:
            while l < r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if s[r].lower() !=s[l].lower():
                return False
            l+=1
            r-=1
        return True

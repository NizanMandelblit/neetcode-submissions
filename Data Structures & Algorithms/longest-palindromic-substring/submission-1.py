class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
            
        # Create the DP table initialized to False
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_length = 1

        # Single letters are all true dp[i][i] for all i
        for i in range(n):
            dp[i][i] = True

        # 2 sized strings are true iff s[i] == s[i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i  # Fixed: track the actual starting index
                max_length = 2

        # 3 sized and above: s[i]==s[j] and the inner substring is a palindrome
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1 # Ending index
                
                # Fixed: Compare string characters, and look up inner table state
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True  # Fixed: Use '=' for assignment
                    
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start:start+max_length]
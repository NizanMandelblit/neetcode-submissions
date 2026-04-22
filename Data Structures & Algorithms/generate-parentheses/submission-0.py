class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add close if close<open
        # add open 

        # return when open=close=n
        stack = []
        res = []
        def backtrack(closeN,openN):
            if closeN==openN==n:
                res.append("".join(stack))

            if openN<n:
                stack.append('(')
                backtrack(closeN,openN+1)
                stack.pop()
            if closeN<openN:
                stack.append(')')
                backtrack(closeN+1,openN)
                stack.pop()


        backtrack(0,0)

        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >=len(nums):
                # when you do res.append(subset), you are appending a reference to the list, not a snapshot of it. Since you continue to modify that same subset list (via append and pop), every entry in your final res will end up pointing to the same empty list.
                # You need to append a copy of the subset.
                res.append(subset.copy()) 
                return
            
            # include i in subset
            subset.append(nums[i])
            dfs(i+1)

            # don't include i
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

        
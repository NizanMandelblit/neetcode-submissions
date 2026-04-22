class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,curr,total):
            if i >=len(nums) or total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            # include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])  # resuse nums[i]
            curr.pop()
            # don't reuse nums[i]
            dfs(i+1,curr,total)


        dfs(0,[],0)
        return res
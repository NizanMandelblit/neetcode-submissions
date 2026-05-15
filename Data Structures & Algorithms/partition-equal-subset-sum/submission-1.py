class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target = sum(nums)
        # if target%2:
        #     return False

        # def dfs(i, target):
        #     if target == 0:
        #         return True
        #     if i==len(nums):
        #         return False
            
        #     return dfs(i+1,target) or dfs(i+1,target-nums[i])
        
        # return dfs(0,target//2)
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
class Solution:
    def rob(self, nums: List[int]) -> int:
        # https://youtu.be/kIII1uT6F8Y
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        cache = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in cache:
                return cache[i]
            else:
                cache[i] = max(nums[i] + helper(i - 2), helper(i - 1))
                return cache[i]

        return helper(n - 1)

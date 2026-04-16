class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force O(n^3)
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple([nums[i] , nums[j], nums[k]])) # set can't accept list as they can't hash it, so make it a tuple
        
        # return [list(i) for i in res]

        # two pointers
        res = []
        nums.sort()
        i = 0 
        while i < len(nums):
            a = nums[i]
            if a > 0:
                break # all following numbers are positive
            l, r = i + 1, len(nums) - 1
            while l < r:
                tripleSum = a + nums[l] + nums[r]
                if tripleSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif tripleSum > 0:
                    r -= 1
                elif tripleSum < 0:
                    l += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1

        return res
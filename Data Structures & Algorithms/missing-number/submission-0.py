class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # a^a=0
        for i in range(len(nums)+1):
            nums.append(i)
        res = 0 
        for num in nums:
            res^=num
        return res


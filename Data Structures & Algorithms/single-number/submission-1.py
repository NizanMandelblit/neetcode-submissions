class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0 and a ^ 0 = a.
        res = 0
        for num in nums:
            res = res ^ num
        return res

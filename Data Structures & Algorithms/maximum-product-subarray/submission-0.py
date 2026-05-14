class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 is not a good default, for example nums= [-3], so res=-3

        currMax, currMin = 1, 1
        for num in nums:
            temp = currMax*num
            currMax = max(temp, currMin*num, num)
            currMin = min(temp, currMin*num, num)
            res = max(currMax,res)
        
        return res

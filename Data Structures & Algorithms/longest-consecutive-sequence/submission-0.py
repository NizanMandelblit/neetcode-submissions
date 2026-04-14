class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest=0
        for num in nums:
            length=0
            if (num-1) not in numSet:
                while num+length in numSet:
                    length= length+1
                longest=max(longest,length)
        
        return longest
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for num in nums:
            if (hashTable.get(num,0)):
                return True
            hashTable[num] = 1

        return False
#   O(n) space and time
#   to reduce space you can heapsort in O(nlogn) and check every two adjacent cells
#    nums.sort() # Assume an in-place O(1) space sort here (like heapsort)
#        for i in range(len(nums) - 1):
#            if nums[i] == nums[i + 1]:
#                return True
#        return False


#like Python's Timsort or C++ std::sort) that use O(n)$ or O(log n) extra space for recursion stacks or temporary arrays
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}
        # First pass: populate the dictionary
        for i in range(len(nums)):
            valueToIndex[nums[i]] = i

        # Second pass: find the complement
        for i in range(len(nums)):
            desiredValue = target - nums[i]
            
            # Check if complement exists AND is not the current element
            if desiredValue in valueToIndex and valueToIndex[desiredValue] != i:
                return [i, valueToIndex[desiredValue]]
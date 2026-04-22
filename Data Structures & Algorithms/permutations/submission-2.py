class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Recursion Trace for nums = [1, 2, 3]:
        
        | Level | Input `nums` | `perms` (from child) | Resulting `res` (after insertions)
        |-------|--------------|----------------------|----------------------------------
        | Base  | []           | N/A                  | returns [[]]
        | 1     | [3]          | [[]]                 | returns [[3]]
        | 2     | [2, 3]       | [[3]]                | returns [[2,3], [3,2]]
        | 3     | [1, 2, 3]    | [[2,3], [3,2]]       | returns [[1,2,3], [2,1,3], [2,3,1], 
        |       |              |                      |          [1,3,2], [3,1,2], [3,2,1]]
        """
        if len(nums) == 0:
            return [[]]

        # perms holds all permutations of the list excluding the first element
        perms = self.permute(nums[1:])
        res = []
        
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
                
        return res
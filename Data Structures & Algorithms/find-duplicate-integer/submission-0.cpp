class Solution {
public:
    int findDuplicate(vector<int> &nums) {
        // detect cycle intersection using floyds algo
        int slowPtr = nums[0];
        int fastPtr = nums[0];

        // Move slow by 1 step and fast by 2 steps until they meet
        do {
            slowPtr = nums[slowPtr];
            fastPtr = nums[nums[fastPtr]];
        } while (slowPtr != fastPtr);

        // find start of cycle
        int slowPtrSecond = nums[0];
        while (slowPtrSecond != slowPtr) {
            slowPtrSecond = nums[slowPtrSecond];
            slowPtr = nums[slowPtr];
        }

        return slowPtr;
    }
};

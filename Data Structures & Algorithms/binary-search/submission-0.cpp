/*
 * @lc app=leetcode id=704 lang=cpp
 *
 * [704] Binary Search
 */

// @lc code=start
using namespace std;
#include <vector>
class Solution {
  public:
    int search(vector<int> &nums, int target) {
        return binary_search(nums, target, 0, nums.size() - 1);
    }

    int binary_search(vector<int> &nums, int target, int left, int right) {
        if (left > right)
            return -1; // Base case: target not found
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
            return mid;

        if (nums[mid] > target)
            return binary_search(nums, target, left, mid - 1);
        else
            return binary_search(nums, target, mid + 1, right);
    }
};
// @lc code=end

/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
#include <unordered_map>
#include <vector>
class Solution {
  public:
    std::vector<int> twoSum(std::vector<int> &nums, int target) {
        std::unordered_map<int, int> hashMap; // maps val to index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (hashMap.count(complement))
                return {hashMap[complement], i };

            hashMap[nums[i]] = i;
        }
        return {};
    }
};
// @lc code=end

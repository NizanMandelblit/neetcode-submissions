/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

// @lc code=start
// #include <vector>
// using namespace std;
class Solution {
  public:
    void backtrack(vector<vector<int>> &res,
                   vector<int> &nums,
                   vector<int> &permutation,
                   vector<bool> &used) {
        // goal
        if (permutation.size() == nums.size()) {
            res.push_back(permutation);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!used[i]) {
                // choice
                used[i] = true;
                permutation.push_back(nums[i]);
                backtrack(res, nums, permutation, used);
                // undo choice
                used[i] = false;
                permutation.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int> &nums) {
        vector<vector<int>> res{};
        vector<int> permutation{};
        vector<bool> used(nums.size(), false);
        backtrack(res, nums, permutation, used);
        return res;
    }
};
// @lc code=end

/*
 * @lc app=leetcode id=875 lang=cpp
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
#include <algorithm> // for std::max_element
#include <vector>
using namespace std;
class Solution {
  public:
    int minEatingSpeed(vector<int> &piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        while (left < right) {
            int middle = left + (right - left) / 2;
            int hours = 0;
            for (auto &&num_banna : piles)
                hours += (num_banna + middle - 1) / middle; // round up
            if (hours <= h)
                right = middle; // Middle could be the result, so try to reduce the speed
            else
                left = middle + 1; // increase speed
        }

        return left; // Smallest speed at which Koko can finish in h hours
    }
};
// @lc code=end
